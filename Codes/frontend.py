#!/usr/bin/env python
# coding: utf-8

# In[2]:





# In[1]:


import streamlit as st
import pandas as pd
import plotly.graph_objects as go


# In[2]:


st.set_page_config(
    page_title="Inventory Reorder Dashboard",
    layout="centered"
)

st.title("Inventory Reorder Decision Tool")
st.markdown("**Store:** S001")


#Loading data

@st.cache_data
def load_data():
    return pd.read_csv(
        r"C:\Users\MAITHILI\Personal_project\Datasets\inventory_decision_output.csv"
    )

df = load_data()


#Selecting the product

product_list = sorted(df['Product_ID'].unique())
selected_product = st.selectbox("Select Product", product_list)

product_df = df[df['Product_ID'] == selected_product].iloc[0]


#Displaying the metrics

col1, col2, col3 = st.columns(3)

col1.metric(
    label="Current Inventory",
    value=int(product_df['Current_Inventory'])
)

col2.metric(
    label="Reorder Point",
    value=int(product_df['Reorder_Point'])
)

col3.metric(
    label="Safety Stock",
    value=int(product_df['Safety_Stock'])
)


#Inventory Status

st.subheader(" Inventory Status")

if product_df['Inventory_Status'] == "REORDER NOW":
    st.error("🚨 REORDER NOW")
    st.metric(
        label="Recommended Order Quantity (EOQ)",
        value=int(product_df['Order_Quantity'])
    )
else:
    st.success("✅ Inventory Level is OPTIMAL")


#Gauge Chart

st.subheader("📊 Inventory Level Gauge")

max_stock = product_df['Max_Stock_Level']
current_stock = product_df['Current_Inventory']

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=current_stock,
    title={'text': "Stock Level"},
    gauge={
        'axis': {'range': [0, max_stock]},
        'bar': {'color': "darkblue"},
        'steps': [
            {'range': [0, product_df['Reorder_Point']], 'color': "lightcoral"},
            {'range': [product_df['Reorder_Point'], max_stock], 'color': "lightgreen"}
        ],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': product_df['Reorder_Point']
        }
    }
))

st.plotly_chart(fig, use_container_width=True)


#Product Summary

st.subheader("Product Summary")

summary_df = pd.DataFrame({
    "Metric": [
        "ABC Category",
        "Avg Daily Demand",
        "EOQ",
        "Max Stock Level"
    ],
    "Value": [
        product_df['ABC_Category'],
        round(product_df['Avg_Daily_Demand'], 2),
        int(product_df['EOQ']),
        int(product_df['Max_Stock_Level'])
    ]
})

st.table(summary_df)




