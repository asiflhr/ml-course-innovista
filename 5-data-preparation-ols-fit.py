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