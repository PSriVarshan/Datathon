import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# Page Title
st.title("Sales Over Time by Category")

# Load Sales Model and Data
@st.cache_data
def load_data():
    # Load the pre-processed data (assuming you have a CSV with this format)
    data = pd.read_csv('data/sales.csv', encoding='ISO-8859-1')  # Specifying encoding
    return data

# Function to plot sales by category
def plot_sales_over_time(data, category):
    plt.figure(figsize=(14, 7))
    
    # Filter data by category
    category_data = data[data['Category Name'] == category]
    
    # Plot the sales data over time
    plt.plot(category_data['order date (DateOrders)'], category_data['Sales'], marker='o', label=category)
    
    # Customize the plot
    plt.title(f'Sales Over Time for {category}')
    plt.xlabel('Order Date')
    plt.ylabel('Total Sales Value')
    plt.legend(title='Category Name')
    plt.grid(True)
    
    # Show plot in Streamlit
    st.pyplot(plt)

# Load data
sales_data = load_data()

# Sidebar for category selection
category_options = sales_data['Category Name'].unique()
selected_category = st.sidebar.selectbox('Select Category', category_options)

# Display the sales plot for the selected category
st.write(f"## Sales Data for {selected_category}")
plot_sales_over_time(sales_data, selected_category)
