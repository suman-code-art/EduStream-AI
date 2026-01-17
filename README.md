# EduStream-AI 🎓

EduStream-AI is an AI-powered Class 10 stream counselling system that analyzes student academic performance using Machine Learning and recommends the most suitable stream: **Science, Commerce, or Arts**.

---

## 🔍 Problem Statement
Many students face difficulty choosing the right academic stream after Class 10 due to lack of proper guidance. This project aims to provide **data-driven, unbiased, and explainable recommendations** using machine learning.

---

## 📊 Datasets Used
- **UCI Student Performance Dataset**
- **Kaggle Students Performance Dataset**

These datasets were cleaned, preprocessed, and combined to form a unified counselling dataset:
- `class10_stream_counselling_final.csv`

---

## ⚙️ Features Considered
- Academic strength (average performance)
- Subject-wise scores (Math, English, Science)
- Failure history (consistency)
- Language inclination
- Mathematical inclination

---

## 🧠 Machine Learning Model
- Algorithm: **Random Forest Classifier**
- Library: **scikit-learn**
- Label Encoding used for target classes
- Model evaluated using accuracy, confusion matrix, and classification report

---

## 🌐 System Architecture
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask + Flask-CORS
- **ML Model Serving:** Joblib
- **Integration:** REST API (`/predict` endpoint)

---

## ✅ Backend Verification
The backend was tested using a POST request and successfully returned predictions such as:

