"""
Create the interface before run a code , here we are going to use streamlit page method
"""
#
# import streamlit as st
# st.title("Weather forecast for the next days")
# place=st.text_input("Enter your place here: ")
# days=st.slider("Forcast Days",min_value=1,max_value=5)
# option = st.selectbox("select data to view",("TEMPERATURE","SKY"))
# st.subheader(f"{option} for the next {days} days in {place}")


"""
Now here we are going to add graph 
"""

# import streamlit as st
# import plotly.express as px
# st.title("Weather forecast for the next days")
# place=st.text_input("Enter your place here: ")
# days=st.slider("Forcast Days",min_value=1,max_value=5)
# option = st.selectbox("select data to view",("TEMPERATURE","SKY"))
# st.subheader(f"{option} for the next {days} days in {place}")
#
# dates=["2026-20-05","2026-21-05","2026-22-05"]
# temperature = [10,15,25]
# temperature = [days*i for i in temperature]
#
# fiqure = px.line(x=dates,y=temperature ,labels={'x':'Date','y':'Temperature'})
# st.plotly_chart(fiqure)

"""
fake the plot data dynamicallly ( hardcode data for checking like working fine or not) and using function for actual maner thats why
"""

# import streamlit as st
# import plotly.express as px
# st.title("Weather forecast for the next days")
# place=st.text_input("Enter your place here: ")
# days=st.slider("Forcast Days",min_value=1,max_value=5)
# option = st.selectbox("select data to view",("TEMPERATURE","SKY"))
# st.subheader(f"{option} for the next {days} days in {place}")
#
# def get_data(days):
#     dates = ["2026-20-05", "2026-21-05", "2026-22-05"]
#     temperature = [10, 15, 25]
#     temperature = [days * i for i in temperature]
#     return dates, temperature
#
# d,t= get_data(days)
#
# fiqure = px.line(x=d,y=t ,labels={'x':'Date','y':'Temperature(C)'})
# st.plotly_chart(fiqure)

"""
Then do exercise in student project thats it
"""