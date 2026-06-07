# import requests
# API_key="1e2d77be33e2256ac0ac30c2e03131ee"
#
# def get_data(place,days,option):
#     url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
#     response = requests.get(url)
#     data = response.json()
#     return data
#
# if __name__=="__main__":
#     result = get_data(place="Chennai",days=None,option=None)
#     print(result)

"""
Filtering the data - using debug method to solve this ,
use red dot on above return data then give debug open and use how ever you want
"""

# import requests
# API_key="1e2d77be33e2256ac0ac30c2e03131ee"
#
# def get_data(place,days,kind):
#     url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
#     response = requests.get(url)
#     data = response.json()
#     filtered_data=data["list"]
#     nr_values = 8 * days # one day 24 hour right,  this api split 3 section(upto 5 days , 3 hour once one data) , so we get 8 day in a row
#     filtered_data=filtered_data[:nr_values]
#     if kind == "TEMPERATURE":
#         filtered_data=[i['main']['temp'] for i in filtered_data]
#     if kind == "SKY":
#         filtered_data = [i['weather'][0]['main'] for i in filtered_data]
#
#     return filtered_data
#
# if __name__=="__main__":
#     result = get_data(place="Chennai",days=2,kind="SKY")
#     print(result)

"""
Add sky conditions here
"""

import requests
API_key="1e2d77be33e2256ac0ac30c2e03131ee"

def get_data(place,days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data=data["list"]
    nr_values = 8 * days
    filtered_data=filtered_data[:nr_values]
    # if kind == "TEMPERATURE":
    #     filtered_data=[i['main']['temp'] for i in filtered_data]
    # if kind == "SKY":
    #     filtered_data = [i['weather'][0]['main'] for i in filtered_data]

    return filtered_data

if __name__=="__main__":
    result = get_data(place="Chennai",days=2)
    print(result)
