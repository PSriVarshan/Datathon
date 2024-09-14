import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard",
                    page_icon=":compass:",
                    layout="wide")


df = pd.read_csv(r'data\app.csv', encoding='ISO-8859-1')



    # Default page content (e.g., intro, instructions, etc.)
st.title("Welcome to the Supply Chain Optimization Platform")
st.write("""
    Select a model from the sidebar to begin working with the different optimization models. 
    Each model provides insights into various aspects of supply chain management, such as sales prediction, pricing, inventory, and profit calculations.
""")



st.sidebar.header("Please Filter Here:")
dept = st.sidebar.multiselect(
    "Select the Department Name:",
    options=df["Department_Name"].unique(),
    default=df["Department_Name"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Segment",
    options=df["Customer_Segment"].unique(),
    default=df["Customer_Segment"].unique()
)

ship = st.sidebar.multiselect(
    "Select the Shipping Mode:",
    options=df["Shipping_Mode"].unique(),
    default=df["Shipping_Mode"].unique()
)



df_selection = df.query(
    "Department_Name == @dept & Customer_Segment ==@customer_type & Shipping_Mode == @ship"
)

if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop()

st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

st.markdown("---")

sales_by_dept=(
    df.groupby(by=["Department_Name"]).sum()[["Sales"]].sort_values(by="Sales")
)

fig_prod = px.bar(
    sales_by_dept,
    x="Sales",
    y=sales_by_dept.index,
    orientation="h",
    title="<b>Sales by Department</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_dept),
    template="plotly_white",
)

fig_prod.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)