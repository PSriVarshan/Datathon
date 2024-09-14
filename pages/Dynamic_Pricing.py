import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
try:
    df = pd.read_csv(r'data\data.csv', encoding='ISO-8859-1')
    st.success("Data is loading, please wait, the data is large")
except FileNotFoundError:
    st.error("The file data\data.csv was not found.")
    st.stop()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Define feature columns and target
features = ['Order Item Product Price', 'Order Item Discount', 'Order Item Quantity', 
            'Product Price', 'Benefit per order']
target = 'Sales'

# Check if the dataset contains the required columns
missing_columns = [col for col in features + [target] if col not in df.columns]
if missing_columns:
    st.error(f"The following required columns are missing from the dataset: {', '.join(missing_columns)}")
    st.stop()

# Train the model
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Streamlit App
st.title("Sales Prediction App")

# Input features
order_item_product_price = st.number_input("Price of products without discount (previous amount)", min_value=0.0)
order_item_discount = st.number_input("Order Item Discount (not in percentage)", min_value=0.0)
order_item_quantity = st.number_input("Number of products per order", min_value=1)
product_price = st.number_input("Product Price", min_value=0.0)
benefit_per_order = st.number_input("Earnings per order, i.e., profit after discounts, costs, etc.", min_value=0.0)

# Make prediction on button click
if st.button("Predict Sales"):
    new_data = pd.DataFrame({
        'Order Item Product Price': [order_item_product_price],
        'Order Item Discount': [order_item_discount],
        'Order Item Quantity': [order_item_quantity],
        'Product Price': [product_price],
        'Benefit per order': [benefit_per_order],
    })
    
    try:
        predicted_sales = model.predict(new_data)
        st.subheader(f"Predicted      s: ${predicted_sales[0]:.2f}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
