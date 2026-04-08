# 🏠 House Price Prediction using Linear Regression

## 📌 Project Overview

This project implements a **Linear Regression model** to predict house prices based on:

* Square Footage (GrLivArea)
* Number of Bedrooms
* Number of Bathrooms

The model is trained using the **Kaggle House Prices dataset** and deployed as an interactive web application using Streamlit.

---

## 🎯 Objective

To build a machine learning model that predicts house prices and provide a user-friendly interface for real-time predictions.

---

## 📂 Dataset

Dataset used: *House Prices - Advanced Regression Techniques*

Files used:

* `train.csv` → Training data
* `test.csv` → Testing data

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 🧠 Machine Learning Model

* Algorithm: **Linear Regression**
* Target Variable: `SalePrice`
* Features Used:

  * GrLivArea (Square Footage)
  * BedroomAbvGr (Bedrooms)
  * FullBath (Bathrooms)

---

## 🚀 How It Works

1. Data is loaded and preprocessed
2. Relevant features are selected
3. Model is trained using Linear Regression
4. Model is saved using pickle
5. Streamlit app takes user input and predicts house price

---

## 💻 Streamlit App Features

* User-friendly interface
* Input sliders for:

  * Square Footage
  * Bedrooms
  * Bathrooms
* Real-time price prediction

---

## 📸 Output Example

* Input: 1500 sqft, 3 bedrooms, 2 bathrooms
* Output: Estimated house price 💰

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deployment

The app is deployed using **Streamlit Cloud** and accessible via a public URL.

---

## 📌 Conclusion

This project demonstrates how Linear Regression can be used for real-world prediction tasks and deployed as a web application.

---

## 🙌 Author

Developed as part of Machine Learning Internship (SkillCraft Technology)
