import streamlit as st
import pandas as pd

df = pd.read_csv("data/SampleSuperstore.csv")

st.title("RetailPulse Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", round(df["Sales"].sum(), 2))

with col2:
    st.metric("Total Profit", round(df["Profit"].sum(), 2))

with col3:
    st.metric("Average Sales", round(df["Sales"].mean(), 2))
st.subheader("Sales by Category")

sales_by_category = df.groupby("Category")["Sales"].sum()

st.bar_chart(sales_by_category)

st.subheader("Profit by Category")

profit_by_category = df.groupby("Category")["Profit"].sum()

st.bar_chart(profit_by_category)

st.subheader("Top 10 States by Sales")

top_states = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

st.bar_chart(top_states)
st.subheader("Top 10 Sub-Categories by Sales")

subcat_sales = (
    df.groupby("Sub-Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

st.bar_chart(subcat_sales)
st.subheader("Top 10 Sub-Categories by Profit")

subcat_profit = (
    df.groupby("Sub-Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

st.bar_chart(subcat_profit)
st.subheader("Sales by Region")

region_sales = df.groupby("Region")["Sales"].sum()

st.bar_chart(region_sales)
st.sidebar.header("Filters")

selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + list(df["Region"].unique())
)

if selected_region != "All":
    df = df[df["Region"] == selected_region]


selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(df["Category"].unique())
)

if selected_category != "All":
    df = df[df["Category"] == selected_category]