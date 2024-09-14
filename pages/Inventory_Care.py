import streamlit as st

# Page Title
st.title("Reorder Point (ROP) Calculator")

# Sidebar for input values
st.sidebar.header('Input Parameters')

# Function to get user input
def user_input_features():
    demand_rate = st.sidebar.number_input('Daily Demand Rate (units per day)', min_value=0.0, value=10.0)
    lead_time = st.sidebar.number_input('Lead Time (days)', min_value=0.0, value=5.0)
    safety_stock = st.sidebar.number_input('Safety Stock (units)', min_value=0.0, value=10.0)
    stock = st.sidebar.number_input('Present Stock', min_value=0, value=10)
    
    data = {
        'Demand Rate': demand_rate,
        'Lead Time': lead_time,
        'Safety Stock': safety_stock,
        'Stock': stock,
    }
    return data

# Get the input data from the user
input_data = user_input_features()

# Reorder Point calculation
def calculate_rop(demand_rate, lead_time, safety_stock):
    # ROP formula: (demand rate * lead time) + safety stock
    reorder_point = (demand_rate * lead_time) + safety_stock
    return reorder_point

# Calculate the Reorder Point (ROP) and check if inventory is fine or if reorder is needed
if st.button('Calculate Reorder Point'):
    demand_rate = input_data['Demand Rate']
    lead_time = input_data['Lead Time']
    safety_stock = input_data['Safety Stock']
    stock = input_data['Stock']
    
    reorder_point = calculate_rop(demand_rate, lead_time, safety_stock)
    
    st.subheader(f"The Reorder Point (ROP) is: {reorder_point:.2f} units")
    
    # Display a message based on the current inventory level
    if stock < reorder_point:
        st.error(f"Your current inventory level of { stock:.2f} units is below the Reorder Point. You should reorder now!")
    else:
        st.success(f"Your current inventory level of {stock:.2f} units is sufficient. No need to reorder at the moment.")
