import streamlit as st
import pandas as pd

# -------------------------------
# Title and Description
# -------------------------------
st.title("📊 Sales Summary Dashboard")
st.subheader("Filter sales data by category and visualize trends")

# -------------------------------
# Hardcoded DataFrame
# -------------------------------
data = {
    "Product": ["Laptop", "Shirt", "Phone", "Pants", "Tablet", "Shoes"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics", "Clothing"],
    "Sales": [50000, 15000, 30000, 12000, 20000, 18000]
}

df = pd.DataFrame(data)

# -------------------------------
# Sidebar Filter (Task 2)
# -------------------------------
st.sidebar.header("Filter Options")

category = st.sidebar.selectbox(
    "Select Category",
    options=df["Category"].unique()
)

# -------------------------------
# Filter Data
# -------------------------------
filtered_df = df[df["Category"] == category]

# -------------------------------
# Display Filtered Data
# -------------------------------
st.write(f"### Showing data for: {category}")
st.dataframe(filtered_df)

# -------------------------------
# Line Chart
# -------------------------------
st.write("### Sales Trend")
st.line_chart(filtered_df["Sales"])