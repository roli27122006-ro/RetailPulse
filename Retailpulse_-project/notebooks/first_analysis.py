import pandas as pd

df = pd.read_csv("data/SampleSuperstore.csv")

print(df.head())

print("\nRows and Columns:")
print(df.shape)

import pandas as pd

df = pd.read_csv("data/SampleSuperstore.csv")

print(df.head())

print("\nRows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())

print("\nAverage Sales:")
print(df["Sales"].mean())

print("\nAverage Sales:")
print(df["Sales"].mean())

import matplotlib.pyplot as plt

category_sales = df.groupby("Category")["Sales"].sum()

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.show()