import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Load the Dataset
file_path = 'lec_6_auto-mpg.data'
column_names = ['MPG', 'Cylinder', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Modal Year', 'Origin', 'Car Name']
df = pd.read_csv(file_path, sep='\s+', names=column_names, na_values='?')

print("\n Initial data: ")
print(df.head(8))
print(f"\n Total rows and columns before cleaning: {df.shape}")

# Data Preprocessing: Removing missing values
df.dropna(inplace=True)  
print("\n Data after dropping rows with missing values: ")
print(df.head(8))
print(f"\n Total rows and columns after cleaning: {df.shape}")

# Select features
X = df['Horsepower'].values.reshape(-1, 1)
y = df['MPG'].values

# Fit Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X, y)
y_pred_linear = linear_model.predict(X)

# Plot Linear Regression results
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred_linear, color='red', linewidth=2, label='Linear Regression Line')
plt.title('Linear Regression: MPG vs Horsepower')
plt.xlabel('Horsepower')
plt.ylabel('MPG')
plt.legend()
plt.show()

# Evaluate Linear Regression Model
mse_linear = mean_squared_error(y, y_pred_linear)
r2_linear = r2_score(y, y_pred_linear)
print(f"Linear Regression Mean Squared Error (MSE): {mse_linear:.2f}")
print(f"Linear Regression R-Squared (R^2): {r2_linear:.2f}")

# Prepare data for Polynomial Regression (Quadratic)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Fit Polynomial Regression model
poly_model = LinearRegression()
poly_model.fit(X_poly, y)
y_pred_poly = poly_model.predict(X_poly)

# Plot Polynomial Regression results
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='magenta', label='Actual Data')
plt.plot(X, y_pred_poly, color='green', linewidth=2, label='Quadratic Regression Line')
plt.title('Quadratic Regression: MPG vs Horsepower')
plt.xlabel('Horsepower')
plt.ylabel('MPG')
plt.legend()
plt.show()

# Evaluate Polynomial Regression Model
mse_poly = mean_squared_error(y, y_pred_poly)
r2_poly = r2_score(y, y_pred_poly)
print(f"Quadratic Regression Mean Squared Error (MSE): {mse_poly:.2f}")
print(f"Quadratic Regression R-squared (R^2): {r2_poly:.2f}")

# Compare model performance
print(f"Improvement in R-squared from Linear to Quadratic Regression: {r2_poly - r2_linear:.2f}")
print(f"Reduction in MSE from Linear to Quadratic Regression: {mse_linear - mse_poly:.2f}")

while True:
    # Prediction using LInear Regression Model
    horsepower_input = float(input("Enter the horsepower for Linear Regression prediction: "))
    predicted_mpg_linear = linear_model.predict([[horsepower_input]])
    print(f"Predicted MPG using Linear Regression for Horsepower = {horsepower_input}: {predicted_mpg_linear[0]:.2f}")
    
    # Prediction using Polynomial Regression Model
    predicted_mpg_poly = poly_model.predict(poly.transform([[horsepower_input]]))
    print(f"Predicted MPG using Quadratic Regression for Horsepower = {horsepower_input}: {predicted_mpg_poly[0]:.2f}")
    doAgain = input(f"If you want to predict again for some other value press y otherwise press n: ")
    if doAgain =='n':
        break

    