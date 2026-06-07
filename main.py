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
Then do exercise in student project student_project.py thats it
"""

"""
We didnt finsih yet, here we are going to see Getting Raw Forecast Data,
lets look at the backend.py file where api data extracter from api
"""

"""
Filtering data from raw file in backend.py
"""

# from backend import get_data
# import streamlit as st
# import plotly.express as px
# st.title("Weather forecast for the next days")
# place=st.text_input("Enter your place here: ")
# days=st.slider("Forcast Days",min_value=1,max_value=5)
# option = st.selectbox("select data to view",("TEMPERATURE","SKY"))
# st.subheader(f"{option} for the next {days} days in {place}")
#
# #here we are going to use if condition , no need to use there in backend.py so remove them
# if place: #if input box empty means we got some error like list error so we add place  condition ,
#     # if place value exist only it would run further thats it
#
#     filtered_data = get_data(place, days)
#     if option == "TEMPERATURE":
#         temperature = [i['main']['temp'] for i in filtered_data]
#         dates = [i['dt_txt'] for i in filtered_data]
#         fiqure = px.line(x=dates, y=temperature, labels={'x': 'Date', 'y': 'Temperature(C)'})
#         st.plotly_chart(fiqure)
#
#     if option == "SKY":
#         images={'Clear':"images/clear.png",
#                 'Clouds':"images/cloud.png",
#                 'Rain':"images/rain.png",
#                 'Snow':"images/snow.png"}
#         sky_conditions = [i['weather'][0]['main'] for i in filtered_data]
#         image_path=[images[i] for i in sky_conditions]
#         st.image(image_path,width=115)

"""
student project fix the weather app error 
1.showing temperature in full for example : 294, but actuall degree value 29.4 - so we need to change this first
2.if entered location not exist, we get error so fix that , so tell them enter correct loaction
"""

from backend import get_data
import streamlit as st
import plotly.express as px
st.title("Weather forecast for the next days")
place=st.text_input("Enter your place here: ")
days=st.slider("Forcast Days",min_value=1,max_value=5)
option = st.selectbox("select data to view",("TEMPERATURE","SKY"))
st.subheader(f"{option} for the next {days} days in {place}")

#here we are going to use if condition , no need to use there in backend.py so remove them
if place: #if input box empty means we got some error like list error so we add place  condition ,
    # if place value exist only it would run further thats it
    try:
        filtered_data = get_data(place, days)
        if option == "TEMPERATURE":
            temperature = [(i['main']['temp'])/10 for i in filtered_data]
            dates = [i['dt_txt'] for i in filtered_data]
            fiqure = px.line(x=dates, y=temperature, labels={'x': 'Date', 'y': 'Temperature(C)'})
            st.plotly_chart(fiqure)

        if option == "SKY":
            images={'Clear':"images/clear.png",
                    'Clouds':"images/cloud.png",
                    'Rain':"images/rain.png",
                    'Snow':"images/snow.png"}
            sky_conditions = [i['weather'][0]['main'] for i in filtered_data]
            dates = [i['dt_txt'] for i in filtered_data]
            image_path=[images[i] for i in sky_conditions]
            st.image(image_path,width=115,caption=dates)
            st.text(dates)

    except KeyError:
        st.error("Please enter correct location")
    except AttributeError:
        st.error("Please move the slide Further")




