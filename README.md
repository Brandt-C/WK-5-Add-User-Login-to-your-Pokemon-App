# WK-5-Add-User-Login-to-your-Pokemon-App
In continuation with this week's homework, your task tonight is to build a form for a user to input data and persist that data into your Pokemon App.

You will need to create the following:
Inside of the blueprint folder for "authentication" (assuming the name is "authentication"):
     - 2 routes: One for "signup" and one for "login"
- 2 User Model with the basic infomation listed:
- ID
- First_name
- Last_name
- email
- password
- date_created
- 2 Form with the following information:
- email
- password
- submit_button
- 1 .env file: to add your DATABASE_URL

Note: You may add more to your Form/Model if you would like, but the min is listed above.

HINT: You will need to add the following dependencies to your virtual environment
- pip install Flask-Login
- pip install Flask-WTF
- pip install Flask-Migrate
- pip install psycopg2
- pip install psycopg2-binary -- For those on mac machines
- pip install email-validator -- Verification of emails inside of forms
- pip install python-dotenv
