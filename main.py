"""
Create the interface before run a code , here we are going to use streamlit page method
"""

import streamlit as st
st.title("Weather forecast for the next days")
place=st.text_input("Enter your place here: ")
days=st.slider("Forcast Days",min_value=1,max_value=5)
option = st.selectbox("select data to view",("TEMPERATURE","SKY"))
st.subheader(f"{option} for the next {days} days in {place}")
