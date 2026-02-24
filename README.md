# Crop-Recommendation-System

This repository contains a machine learning-based Crop Recommendation System designed to help farmers optimize agricultural productivity by suggesting the most suitable crops based on environmental factors. The project includes a full data science pipeline—from exploratory data analysis to a functional desktop application.

Features
Machine Learning Pipeline: Data preprocessing, feature scaling, and model training using Random Forest and Logistic Regression.

Environmental Analysis: Recommends crops based on Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, and Rainfall.

Secure Desktop UI: A Tkinter-based dashboard with a login system for authenticated access.

Real-time Prediction: Integrated model loading via joblib for instant crop suggestions based on user input.

Tech Stack
Language: Python

Data Science: Pandas, NumPy, Scikit-Learn

Visualization: Matplotlib, Seaborn

GUI: Tkinter

Model Storage: Joblib

Usage
Login: Use the default credentials (Username: admin, Password: 1234) to access the dashboard.

Input Data: Enter soil nutrients (N, P, K) and climate data (Temperature, Humidity, pH, Rainfall).

Predict: Click the "Predict Crop" button to see the machine learning recommendation

Dataset Overview
The model is trained on parameters including:

N-P-K: Ratio of Nitrogen, Phosphorous, and Potassium content in soil.

Climate: Temperature (C), Humidity (%), and Rainfall (mm).

Soil: pH value of the soil.

Labels: 22 different crops including rice, maize, coffee, and more.
