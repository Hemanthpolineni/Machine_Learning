import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\polin\Desktop\Python\0 Regression Analysis Final\Practice\SLR\SLR.csv")
print(df.isna().sum())

X = df.iloc[:,:-1]
Y = df.iloc[:,-1]
scaler = StandardScaler()
x_scaled = scaler.fit_transform(X)
model = LinearRegression()
model.fit(x_scaled,Y)

val =float(input("Enter Your Experience in year : "))

x_test = np.array([[val]])
test_scaled = scaler.transform(x_test)


Y_pred = model.predict(test_scaled)

print("The Salary for the given experience is",Y_pred)