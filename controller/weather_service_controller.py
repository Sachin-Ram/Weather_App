from flask import Flask,Blueprint,render_template,request,redirect,url_for,flash
from services.weather_services import weather_services


weather_endpoint=Blueprint("weather",__name__,template_folder="templates")

@weather_endpoint.route('/')

def func():

    city=request.args.get("city")

    if request.method=="GET" and not city:

        flash("city name is required","error")

        return render_template("index.html", weather_data=None)

    try:

        data=weather_services(city)


        response=data.get_weather()


        if "main" not in response:
            flash("Weather data not available. Please check the city name.", "error")
            return render_template("index.html", weather_data=None)

        if "weather" not in response:
            flash("Weather description not found. Please try again later.", "error")
            return render_template("index.html", weather_data=None)
        
        weather_data = {
            "city": response["name"],
            "temperature": round(response["main"]["temp"]),  # Convert Kelvin to Celsius
            "description": response["weather"][0]["description"],
            "country": response["sys"]["country"],
        }
        flash("data fetched","success")
        return render_template("index.html",weather_data=weather_data)
    
    except Exception as e:

        flash("We're sorry, but something went wrong on our end. Please try again later.","error")
        return render_template("index.html", weather_data=None)

@weather_endpoint.route('/test')

def func2():

    data=weather_services(request.args.get("city"))

    response=data.get_weather()

    return response