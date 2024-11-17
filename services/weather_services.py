from flask import Flask,render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class weather_services:

    def __init__(self,city):

        self.api_key=os.getenv('WEATHER_API')

        self.city=city

    def get_lat_long(self):

        response=requests.get("http://api.openweathermap.org/geo/1.0/direct?q={}&appid={}".format(self.city,self.api_key))

        data=response.json()

        return data
    
    def get_weather(self):

        lat_long_data=self.get_lat_long()

        latitude=lat_long_data[0]["lon"]

        longitude=lat_long_data[0]["lat"]

        # weather_data=requests.get("https://api.openweathermap.org/data/2.5/weather?q=${}&units=metric&appid=d82786d494223277eaffb2a4feb1db4b".format(self.city,self.api_key))
        weather_data=requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(self.city,self.api_key))
        result=weather_data.json()

        return result