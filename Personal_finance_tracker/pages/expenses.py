import streamlit as st 
from app import Finance_Tracker 

# 1. Dropdown for categories
FT=Finance_Tracker()
categories = FT.valid_PAY_Category
category = st.selectbox("Select the expense category:", categories)

# If user selects "others", show a text input
if category == "others":
    category = st.text_input("Enter your custom category:")

# 2. Input for amount (numbers only)
amount = st.number_input("Enter the amount spent:", min_value=0.0, step=1.0)

# Display the entered data
if st.button("Submit"):
    if category and amount > 0:
        FT.debit(category,amount)
        st.success(f"Category: {category} | Amount: {amount}")
    else:
        st.error("Please enter valid category and amount.")