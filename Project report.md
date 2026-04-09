# **Autism Prediction using Machine Learning**

## **1. Introduction**

Autism Spectrum Disorder (ASD) is a developmental condition that affects communication and behavior. Early detection plays a crucial role in improving the quality of life through timely intervention. This project aims to develop a machine learning model that can predict the likelihood of autism based on behavioral and personal attributes.

---

## **2. Problem Statement**

Many individuals do not have access to quick and reliable screening tools for autism. The objective of this project is to build a predictive model that can assist in early screening using available data.

---

## **3. Dataset**

The dataset used is an autism screening dataset containing:

* Behavioral scores (A1 to A10)
* Age
* Gender
* Other personal attributes

The target variable is:

* **austim** (Yes/No)

---

## **4. Methodology**

### **4.1 Data Preprocessing**

* Removed unnecessary columns such as ID, age description, and relation
* Converted categorical values into numerical format using encoding
* Handled missing values

### **4.2 Model Selection**

A **Random Forest Classifier** was used because:

* It handles both categorical and numerical data well
* It provides good accuracy
* It helps in identifying feature importance

### **4.3 Training and Testing**

* The dataset was split into training and testing sets (80/20 split)
* The model was trained on the training data
* Predictions were made on the test data

### **4.4 Evaluation**

* Accuracy was used as the evaluation metric

---

## **5. Results**

The model achieved an accuracy of approximately **85%**, indicating good performance in predicting autism likelihood.

Feature importance analysis showed that:

* Age and behavioral scores contributed significantly to the prediction



---

## **6. Conclusion**

This project demonstrates that machine learning can be used as a supportive tool for early autism screening. While the model shows promising accuracy, it is not a substitute for professional medical diagnosis.

---

## **7. Future Scope**

* Use larger and more diverse datasets
* Try advanced models for better accuracy
* Build a user-friendly interface for real-world usage

---

## **8. References**

* Autism Screening Dataset (Kaggle)
* Scikit-learn documentation
