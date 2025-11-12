# 🧠 My Machine Learning Journey

Welcome to my **Machine Learning (ML)** learning journey!  
This repository documents my progress, understanding, and hands-on experiments as I explore ML — from the basics to advanced algorithms.

---

## 📘 What is Machine Learning?

**Machine Learning (ML)** is a subset of **Artificial Intelligence (AI)** that enables computers to learn from data and make predictions or decisions without being explicitly programmed.

Instead of writing rules manually, we provide **data** and let the machine **learn patterns automatically**.

---

## 🔍 Types of Machine Learning

Machine Learning can broadly be categorized into three main types:

1. **Supervised Learning**  
2. **Unsupervised Learning**  
3. **Reinforcement Learning** *(to be added later)*  

---

## 🧩 Supervised Learning

Supervised Learning works with **labeled data**, meaning both **inputs (features)** and **outputs (targets)** are known.  
The model learns a mapping function from input to output by minimizing the prediction error.

### 📂 Subtypes of Supervised Learning

1. **Regression** — Predicts *continuous* values.  
   *(e.g., predicting house prices, temperature, or salary)*  
2. **Classification** — Predicts *categorical* values.  
   *(e.g., spam or not spam, disease or no disease)*  

---

### 📉 Regression Algorithms

#### 1️⃣ Linear Regression
- **Goal:** Find a linear relationship between input variables (X) and the output variable (Y).  
- **Equation:**
  ### Y = mX + c
  
**Where:**
- `Y` = predicted output  
- `X` = input variable  
- `m` = slope or weight  
- `c` = intercept  

**Key Idea:**  
It draws a straight line that best fits the data points by minimizing the sum of squared errors (Least Squares Method).

**Example Use Case:**  
Predicting house prices based on square footage.

---

### 2️⃣ **Multiple Linear Regression**

**Definition:**  
Multiple Linear Regression (MLR) extends simple linear regression by using **two or more independent variables** to predict a dependent variable.

**Equation:**
### Y = b₀ + b₁X₁ + b₂X₂ + ... + bₙXₙ

**Where:**
- `Y` = dependent variable (target)  
- `X₁, X₂, ..., Xₙ` = independent variables (features)  
- `b₀` = intercept  
- `b₁, b₂, ..., bₙ` = coefficients representing the weight of each feature  

**Key Idea:**  
It helps model real-world problems where multiple factors influence the outcome.

**Example Use Case:**  
Predicting car prices based on mileage, brand, engine size, and age.

---

### 3️⃣ **Polynomial Regression**

**Definition:**  
Polynomial Regression is used when the relationship between input and output variables is **non-linear**.  
It models the data as an nth-degree polynomial.

**Equation:**
### Y = b₀ + b₁X + b₂X² + b₃X³ + ... + bₙXⁿ

**Key Idea:**  
It adds polynomial terms (like X², X³) to capture non-linear patterns in the data.

**Example Use Case:**  
Predicting population growth or sales trends that don’t follow a straight line.

---

### 4️⃣ **Ridge Regression (L2 Regularization)**

**Definition:**  
Ridge Regression adds a **penalty term** to the loss function to reduce overfitting by shrinking large coefficients.

**Loss Function:**
### Loss = (Sum of Squared Errors) + λ * (Sum of Squares of Coefficients)


**Key Idea:**  
- Controls model complexity  
- Prevents overfitting when features are highly correlated  

**Example Use Case:**  
Predicting stock prices with many correlated financial indicators.

---

### 5️⃣ **Lasso Regression (L1 Regularization)**

**Definition:**  
Lasso Regression also adds a penalty but uses the **absolute value of coefficients** (L1 norm).  
It can **eliminate less important features** by setting their coefficients to zero.

**Loss Function:**
### Loss = (Sum of Squared Errors) + λ * (Sum of Absolute Values of Coefficients)

**Key Idea:**  
Used for **feature selection** and **sparse models**.

**Example Use Case:**  
Building a model with only the most significant predictors for housing prices.

---

### 6️⃣ **Elastic Net Regression**

**Definition:**  
Elastic Net combines both **L1 (Lasso)** and **L2 (Ridge)** regularization techniques.  
It balances between shrinking coefficients and feature selection.

**Loss Function:**
### Loss = (Sum of Squared Errors) + λ₁ * (Sum of Absolute Values) + λ₂ * (Sum of Squares)

**Key Idea:**  
Useful when there are multiple correlated features.

**Example Use Case:**  
Predicting marketing performance where features overlap (e.g., ads on different platforms).

---

### 7️⃣ **Support Vector Regression (SVR)**

**Definition:**  
SVR is based on the **Support Vector Machine** concept.  
It fits the best line (or hyperplane) within a margin of tolerance (epsilon) while minimizing errors outside that margin.

**Key Idea:**  
- Robust against outliers  
- Works with linear and non-linear data (using kernels)

**Example Use Case:**  
Predicting energy consumption or air quality.

---

### 8️⃣ **Decision Tree Regression**

**Definition:**  
Decision Tree Regression splits data into smaller subsets using decision rules (if/else conditions).  
The final prediction is made by averaging values in each leaf node.

**Key Idea:**  
- Captures non-linear relationships  
- Easy to interpret  
- Can overfit if not pruned

**Example Use Case:**  
Predicting house prices based on various property features.

---

### 9️⃣ **Random Forest Regression**

**Definition:**  
An ensemble of multiple Decision Trees combined to improve accuracy and reduce overfitting.

**Key Idea:**  
Each tree predicts independently, and the final output is the average of all tree predictions.

**Example Use Case:**  
Predicting sales, salaries, or loan default probabilities.

---

### 🔟 **Gradient Boosting Regression**

**Definition:**  
A sequential ensemble technique where each new model corrects errors made by previous ones.  
Popular implementations include **XGBoost**, **LightGBM**, and **CatBoost**.

**Key Idea:**  
- Highly accurate  
- Works well with both linear and non-linear data  
- Sensitive to overfitting if not tuned properly  

**Example Use Case:**  
Predicting customer churn, sales forecasting, or credit scoring.

---

## ⚙️ Summary Table

| Algorithm | Handles Non-Linearity | Regularization | Ensemble | Feature Selection |
|------------|----------------------|----------------|-----------|-------------------|
| Linear Regression | ❌ | ❌ | ❌ | ❌ |
| Multiple Linear Regression | ❌ | ❌ | ❌ | ❌ |
| Polynomial Regression | ✅ | ❌ | ❌ | ❌ |
| Ridge Regression | ❌ | ✅ (L2) | ❌ | ❌ |
| Lasso Regression | ❌ | ✅ (L1) | ❌ | ✅ |
| Elastic Net | ❌ | ✅ (L1 + L2) | ❌ | ✅ |
| SVR | ✅ | ✅ | ❌ | ❌ |
| Decision Tree | ✅ | ❌ | ❌ | ✅ |
| Random Forest | ✅ | ✅ (implicit) | ✅ | ✅ |
| Gradient Boosting | ✅ | ✅ (implicit) | ✅ | ✅ |

---

## 🧠 Key Takeaways
- Use **Linear Regression** for simple, linear relationships.  
- Use **Polynomial Regression** for non-linear patterns.  
- Apply **Ridge/Lasso/Elastic Net** when overfitting occurs or when you need regularization.  
- Use **Tree-based** or **Boosting models** for complex, non-linear, real-world problems.

---

📅 *Last Updated: November 2025*  
👨‍💻 *Author: Hemanth Polineni*

