Contributions of Group mates in this assignment :

1. Amman Ahmed Khan ( API creation, user authentication , dynamically fetching weather info )
2. Sameed Asif ( Database integration )
3. Asim Ayub ( Testing, documentation , requirements ).


"Purpose of the API"
This Flask API integrates various functionalities:

-Weather Data Fetching: It retrieves weather information from the OpenWeatherMap API based on a city name provided via a query parameter.
-User Authentication: It simulates user authentication, returning a JWT (JSON Web Token) upon successful login.
-Password Retrieval: It sends an email for password retrieval using Flask-Mail (Mailtrap is configured as the SMTP server).
-Dynamic URL Handling: It demonstrates basic URL routing, returning custom messages based on path parameters.
-Error Handling: It includes a 404 error handler for resource not found cases.

"How to Install Dependencies and Run the API"
-Clone or Download the Repository: Download the API code to your local machine.

-Install Dependencies: Run the following command to install all required packages from requirements.txt:
pip install -r requirements.txt

-Set Environment Variables: Create a .env file in the root directory and add the following environment variable:
API_KEY=your_openweathermap_api_key
MAIL_USERNAME=your_mailtrap_username
MAIL_PASSWORD=your_mailtrap_password

-Run the API: Once the environment is configured, you can run the Flask API with:
   python app.py

-Access the API: The API will be available locally at http://127.0.0.1:5000/.


"Steps for Testing the API"
1.Weather API Testing:

URL: GET /weather?city=<city_name>
Example:
http://127.0.0.1:5000/weather?city=London
This will display weather information for the specified city in the front-end.


2.Login Endpoint:

URL: POST /login
Example Request (JSON):
json

{
  "email": "test@example.com",
  "password": "password"
}
If successful, it returns a JWT access token.


3.Retrieve Password:

URL: GET /retrieve_password/<email>
Example:
perl
http://127.0.0.1:5000/retrieve_password/test@example.com
This simulates sending a password reset email.


4.Custom URL Handling:
URL: GET /url_variables/<name>/<age>
Example:
arduino
http://127.0.0.1:5000/url_variables/John/25


5.404 Not Found:

URL: GET /not_found
Example:
arduino
http://127.0.0.1:5000/not_found
This returns a 404 error message.
For testing, you can use Postman, cURL, or simply the browser (for GET requests).
