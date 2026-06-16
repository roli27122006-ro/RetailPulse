import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/SampleSuperstore.csv")

# Basic Information
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

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.show()

# Profit by Category
profit_by_category = df.groupby("Category")["Profit"].sum()

print("\nProfit by Category:")
print(profit_by_category)

profit_by_category.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()

# Top 10 States by Sales
top_states = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop 10 States by Sales:")
print(top_states)

top_states.plot(kind="bar")
plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")
plt.show()

# Top 10 Sub-Categories by Sales
subcat_sales = (
    df.groupby("Sub-Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop 10 Sub-Categories by Sales:")
print(subcat_sales)

subcat_sales.plot(kind="bar")
plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")
plt.show()

# Top 10 Sub-Categories by Profit

subcat_profit = (
    df.groupby("Sub-Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop 10 Sub-Categories by Profit:")
print(subcat_profit)

subcat_profit.plot(kind="bar")

plt.title("Top 10 Sub-Categories by Profit")
plt.xlabel("Sub-Category")
plt.ylabel("Profit")

plt.show()

region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(region_sales)

region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()