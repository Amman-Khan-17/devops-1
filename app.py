from flask import Flask, jsonify, request, render_template
import requests
import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager, create_access_token
from flask_mail import Mail, Message

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Configuration
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'  # Set your mail server
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

# Initialize extensions
jwt = JWTManager(app)
mail = Mail(app)

# Get the API key from the environment variable
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


@app.route('/')
def home():
    return render_template('index.html')  # Render the front-end template


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')  # Get city name from URL query parameter
    if not city:
        return render_template('index.html', error='Please provide a city name')  # Return error to front-end

    try:
        # Call OpenWeatherMap API
        response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
        data = response.json()

        # Check if the response is successful
        if response.status_code != 200:
            return render_template('index.html', error=data.get("message", "Error fetching weather data"))

        # Print weather data in terminal in JSON format
        print(f"Weather data for {city}: {data}")

        # Prepare weather data for front-end
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "icon": data["weather"][0]["icon"]  # Get weather icon from OpenWeatherMap
        }

        return render_template('index.html', weather=weather_info)  # Display weather data on the front-end

    except Exception as e:
        return render_template('index.html', error=str(e))  # Handle exceptions


@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name, age):
    if age < 18:
        return jsonify(message=f'You are too young, {name}'), 401
    else:
        return jsonify(message=f'You are old enough, {name}'), 200


@app.route('/not_found')
def not_found():
    return jsonify(message='The resource was not found.'), 404


@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else:
        email = request.form['email']
        password = request.form['password']

    # User authentication logic should go here
    # Simulated response
    if email == "test@example.com" and password == "password":
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid email or password'), 401


@app.route('/retrieve_password/<string:email>', methods=['GET'])
def retrieve_password(email: str):
    # Simulated user lookup logic
    if email == "test@example.com":
        msg = Message('Password Reset', sender=os.getenv('MAIL_USERNAME'), recipients=[email])
        mail.send(msg)
        return jsonify(message='Password reset sent'), 200
    else:
        return jsonify(message='User not found'), 404


if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask application
