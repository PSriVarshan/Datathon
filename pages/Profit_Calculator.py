

import streamlit as st
import numpy as np

# Page Title
st.title("Optimal Price Prediction")

# Sidebar for input values
st.sidebar.header('Input Parameters')

# Function to take user input
def user_input_features():
    order_item_product_price = st.sidebar.number_input('Order Item product price', min_value=0, value=0)
    order_item_discount = st.sidebar.number_input('Order Item Discount', min_value=0, value=0)

    data = {
        'Order Item Product Price': [order_item_product_price],
        'Order Item Discount': [order_item_discount],
    
    }
    return data


input_data = user_input_features()

def predict_optimal_price(input_data):
    product_price = input_data['Order Item Product Price'][0]
    discount = input_data['Order Item Discount'][0]

    optimal_price = ((discount+1)/discount*product_price)+discount
    
    return optimal_price



# Predict the optimal price using the input values
if st.button('Predict Optimal Price'): 
    predicted_price = predict_optimal_price(input_data)
    st.subheader(f'The predicted optimal price is: ${predicted_price:.2f}')

