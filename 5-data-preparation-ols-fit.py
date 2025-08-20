import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
import statsmodels.api as sm
from statsmodels.api import add_constant
import matplotlib.pyplot as plt

def main():
    # Load the Dataset
    file_path = 'lec_5_retail_sales_dataset.csv'
    df = pd.read_csv(file_path)
    print("\n Initial data: ")
    print(df.head(8))
    print(f"\n Total rows and columns before cleaning: {df.shape}")

    # Data Cleaning
    df_cleaned = df.dropna() # Drop rows with missing values
    print("\n Data after dropping rows with missing values: ")
    print(df_cleaned.head(8))
    print(f"\n Total rows and columns after dropping missing values: ")

    # Using SimpleImputer for predictive imputation
    imputer = SimpleImputer(strategy='mean')
    df[['Age', 'Quantity', 'Price per Unit', 'Total Amount']] = imputer
    print("\n Data after imputation: ")
    print("\n ", df.head(8))
    print(f"\n Total rows and columns after imputation: {df.shape}")

    # Handling Categorical Data
    # Label Encoding for Gender
    le = LabelEncoder()
    df["Gender"] = le.fit_transform(df['Gender'])
    print("\n Data after Label Encoding for Gender: ")
    print("\n ", df[['Gender']].head())

    # One-Hot Encoding for Product Category
    df_encoded = pd.get_dummies(df, columns=["Product Category"])
    print("\n Data after One-Hot Encoding for Product Category: ")
    print("\n ", df_encoded.head())

    # Normalizing and Scaling Data
    # Min-Max Scaling
    scaler = MinMaxScaler()
    df[['Quantity', 'Price per Unit', 'Total Amount']] = scaler.fit_transform(df[['Quantity', 'Price per Unit', 'Total Amount']])
    print("\n Data after Min-Max Scaling: ")
    print("\n ", df[['Quantity', 'Price per Unit', 'Total Amount']].head())

    # Standardization
    standard_scaler = StandardScaler()
    df[['Age', 'Quantity', 'Price per Unit', 'Total Amount']] = standard_scaler.fit_transform(df[['Age', 'Quantity', 'Price per Unit', 'Total Amount']])
    print("\n Data after Standardization:")
    print("\n ", df[['Age', 'Quantity', 'Price per Unit', 'Total Amount']].head())
    print("\n Press any key to continue. \n")
    input()

    # Prepairing data for OLS Regression
    X = df[['Price per Unit']] # Independent variable
    y = df[['Total Amount']] # Dependent variable

    # Adding a constant term for intercept
    X = sm.add_constant(X)

    # Fitting the OLS model
    model = sm.OLS(y, X).fit()
    print("\n Press any key to continue. \n")
    input()
    # Summary of the model
    print(model.summary())
    print("\n Press any key to continue. \n")
    input()

    # Scatter plot regression line
    plt.scatter(df['Price per Unit'], df['Total Amount'], color='blue')
    plt.plot(df['Price per Unit'], model.predict(X), color='red', label='')
    plt.xlabel('Independent Variable (Price per Unit)')
    plt.ylabel('Total Amount')
    plt.legend()
    plt.title('Scatter Plot with Regression Line')
    plt.show()

if __name__ == "__main__":
    main()