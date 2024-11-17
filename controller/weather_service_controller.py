from flask import Flask,Blueprint,render_template,request
from services.weather_services import weather_services


weather_endpoint=Blueprint("weather",__name__,template_folder="templates")

@weather_endpoint.route('/')

def func():

    data=weather_services(request.args.get("city"))

    response=data.get_weather()


    weather_data = {
        "city": response["name"],
        "temperature": round(response["main"]["temp"]),  # Convert Kelvin to Celsius
        "description": response["weather"][0]["description"],
        "country": response["sys"]["country"],
    }



    return render_template("index.html",weather_data=weather_data)

@weather_endpoint.route('/test')

def func2():

    data=weather_services(request.args.get("city"))

    response=data.get_weather()

    return response