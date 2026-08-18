# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project predicts house prices based on three important features:

- Area (sq ft)
- Number of Bedrooms
- Age of the House

A Linear Regression machine learning model is trained on the house price dataset and deployed as an interactive Streamlit web application.

## 🎯 Objective

The objective of this project is to build a simple machine learning application that can predict the price of a house based on user-provided property details.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## 📊 Features

The model uses the following input features:

| Feature | Description |
|---|---|
| Area | Area of the house in square feet |
| Bedrooms | Number of bedrooms |
| Age | Age of the house |

## 🤖 Machine Learning Model

**Linear Regression** is used to predict the house price.

The basic workflow is:

```text
House Price Dataset
        ↓
Data Preparation
        ↓
Train-Test Split
        ↓
Linear Regression
        ↓
Model Evaluation
        ↓
Save Model (.pkl)
        ↓
Streamlit Application
        ↓
House Price Prediction
