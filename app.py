from flask import Flask,render_template
from controller.weather_service_controller import weather_endpoint
from dotenv import load_dotenv
import os
load_dotenv()


app=Flask(__name__)

app.secret_key=os.getenv("secret_key")

app.register_blueprint(weather_endpoint)


if __name__=="__main__":

    app.run(debug=True)