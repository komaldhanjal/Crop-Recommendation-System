from tkinter import *
from tkinter import messagebox
import joblib
import pandas as pd

# ==================================================
# LOAD TRAINED FILES
# ==================================================
model = joblib.load("crop_recommendation_model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")   # ✅ FINAL FIX

# ==================================================
# LOGIN FUNCTION
# ==================================================
def login():
    if username_entry.get() == "admin" and password_entry.get() == "1234":
        login_win.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# ==================================================
# DASHBOARD
# ==================================================
def open_dashboard():
    dash = Tk()
    dash.title("Smart Agriculture Dashboard")
    dash.geometry("720x500")
    dash.configure(bg="#0f172a")
    dash.resizable(False, False)

    Label(
        dash,
        text="🌾 Smart Agriculture Dashboard",
        font=("Segoe UI", 22, "bold"),
        bg="#0f172a",
        fg="#38bdf8"
    ).pack(pady=25)

    frame = Frame(dash, bg="#020617")
    frame.pack(padx=60, pady=30, fill=BOTH, expand=True)

    Button(
        frame,
        text="🌱 Crop Recommendation",
        font=("Segoe UI", 15, "bold"),
        bg="#38bdf8",
        fg="#020617",
        height=2,
        relief=FLAT,
        command=lambda: open_crop_ui(dash)
    ).pack(fill=X, padx=50, pady=40)

    Button(
        frame,
        text="🚪 Logout",
        font=("Segoe UI", 12),
        bg="#ef4444",
        fg="white",
        height=2,
        relief=FLAT,
        command=dash.destroy
    ).pack(fill=X, padx=50)

    dash.mainloop()

# ==================================================
# CROP RECOMMENDATION UI
# ==================================================
def open_crop_ui(parent):
    win = Toplevel(parent)
    win.title("Crop Recommendation System")
    win.geometry("840x560")
    win.configure(bg="#0f172a")
    win.resizable(False, False)

    Label(
        win,
        text="🌱 Crop Recommendation System",
        font=("Segoe UI", 20, "bold"),
        bg="#0f172a",
        fg="#38bdf8"
    ).pack(pady=20)

    frame = Frame(win, bg="#020617")
    frame.pack(padx=40, pady=10, fill=BOTH, expand=True)

    inputs = {}
    fields = [
        ("Nitrogen (N)", "N"),
        ("Phosphorus (P)", "P"),
        ("Potassium (K)", "K"),
        ("Temperature (°C)", "temperature"),
        ("Humidity (%)", "humidity"),
        ("pH Value", "ph"),
        ("Rainfall (mm)", "rainfall")
    ]

    for i, (label, key) in enumerate(fields):
        Label(frame, text=label, bg="#020617", fg="white",
              font=("Segoe UI", 11)).grid(row=i, column=0, padx=25, pady=10, sticky="w")

        entry = Entry(frame, bg="#1e293b", fg="white",
                      insertbackground="white", font=("Segoe UI", 11), relief=FLAT)
        entry.grid(row=i, column=1, padx=25, pady=10, ipady=4)
        inputs[key] = entry

    result_box = Text(
        frame,
        height=6,
        width=55,
        bg="#020617",
        fg="#38bdf8",
        font=("Segoe UI", 12),
        relief=FLAT
    )
    result_box.grid(row=9, column=0, columnspan=2, pady=20)

    # ==================================================
    # FINAL CORRECT PREDICTION FUNCTION
    # ==================================================
    def predict_crop():
        try:
            values = [
                float(inputs["N"].get()),
                float(inputs["P"].get()),
                float(inputs["K"].get()),
                float(inputs["temperature"].get()),
                float(inputs["humidity"].get()),
                float(inputs["ph"].get()),
                float(inputs["rainfall"].get())
            ]

            df = pd.DataFrame([values],
                              columns=['N','P','K','temperature','humidity','ph','rainfall'])

            scaled = scaler.transform(df)

            pred = model.predict(scaled)
            crop_name = encoder.inverse_transform(pred)[0]   # ✅ FINAL FIX

            result_box.delete("1.0", END)
            result_box.insert(END, "🌾 Recommended Crop\n\n")
            result_box.insert(END, f"✔ {crop_name}")

        except Exception as e:
            messagebox.showerror("Prediction Error", str(e))

    Button(
        frame,
        text="🔍 PREDICT CROP",
        font=("Segoe UI", 14, "bold"),
        bg="#38bdf8",
        fg="#020617",
        relief=FLAT,
        command=predict_crop
    ).grid(row=8, column=0, columnspan=2, pady=15, ipadx=20, ipady=8)

# ==================================================
# LOGIN UI
# ==================================================
login_win = Tk()
login_win.title("Smart Agriculture Login")
login_win.geometry("460x450")
login_win.configure(bg="#0f172a")
login_win.resizable(False, False)

card = Frame(login_win, bg="#020617")
card.place(relx=0.5, rely=0.5, anchor=CENTER, width=360, height=360)

Label(card, text="Smart Agriculture", font=("Segoe UI", 18, "bold"),
      bg="#020617", fg="#38bdf8").pack(pady=(25, 5))

Label(card, text="Login to continue", font=("Segoe UI", 11),
      bg="#020617", fg="#94a3b8").pack(pady=(0, 20))

Label(card, text="Username", bg="#020617",
      fg="white", font=("Segoe UI", 10)).pack(anchor="w", padx=30)

username_entry = Entry(card, bg="#1e293b", fg="white",
                       insertbackground="white", font=("Segoe UI", 11), relief=FLAT)
username_entry.pack(fill=X, padx=30, pady=(6, 15), ipady=6)

Label(card, text="Password", bg="#020617",
      fg="white", font=("Segoe UI", 10)).pack(anchor="w", padx=30)

password_entry = Entry(card, show="*", bg="#1e293b",
                       fg="white", insertbackground="white",
                       font=("Segoe UI", 11), relief=FLAT)
password_entry.pack(fill=X, padx=30, pady=(6, 20), ipady=6)

Button(card, text="🚀 LOGIN", command=login,
       font=("Segoe UI", 12, "bold"),
       bg="#38bdf8", fg="#020617", relief=FLAT)\
    .pack(fill=X, padx=30, pady=10, ipady=8)

login_win.mainloop()
