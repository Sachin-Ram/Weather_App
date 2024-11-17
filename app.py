from flask import Flask,render_template
from controller.weather_service_controller import weather_endpoint


app=Flask(__name__)


app.register_blueprint(weather_endpoint)


if __name__=="__main__":

    app.run(debug=True)