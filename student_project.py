import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv("happy.csv")
# col=df.columns
# new=[]
# for i in col:
#     i=str(i)
#     upper = i.upper()
#     new.append(upper)
# print(new)

st.title("In search for happiness")
data_x_axis=st.selectbox("select the data for x axis",('HAPPINESS', 'GDP','GENEROSITY'))
data_y_axis=st.selectbox("select the data for y axis",('HAPPINESS', 'GDP','GENEROSITY'))

st.subheader(f"{data_x_axis} and {data_y_axis}")

def get_data(data_x_axis,data_y_axis):
    data_x_axis=data_x_axis.lower()
    data_y_axis=data_y_axis.lower()
    data_x=df[data_x_axis]
    data_y=df[data_y_axis]
    return data_x,data_y

x,y=get_data(data_x_axis,data_y_axis)


figure =px.scatter(x=x,y=y,labels={'x':"data_x_axis",'y':"data_y_axis"})
st.plotly_chart(figure)