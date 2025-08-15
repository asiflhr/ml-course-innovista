import sklearn
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
import statsmodels.api as sm
from statsmodels.api import add_constant
import matplotlib.pyplot as plt

def main():
    # Load the Dataset
    file_path = 'Lecture 5 retail_sales_dataset.csv'
    df = pd.read_csv(file_path)
    print("\n Initial data: ")
    print(df.head(8))
    print(f"\n Total rows and columns before cleaning: {df.shape}")

    # Data Cleaning
    df_cleaned = df.dropna() # Drop rows with missing values
    print("\n Data after dropping rows with missing values: ")