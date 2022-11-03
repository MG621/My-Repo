# Instructions for getting started with Flask

# 1. Install virtualenv
# pip install virtualenv

# 2. Create a virtual environment
# py -m venv flaskEnv
# Here, flaskEnv is a name we chose to give our environment

# 3. Activate the virtual environment
# NOTE: You must be in the directory of your current environment
# source flaskEnv/scripts/activate

# 4. Install Flask in your virtual environment
# pip install flask

from flask import Flask

app = Flask(__name__)

# Create a homepage for the app
@app.route("/")
# When we go to our.URL.com/
    # Then flask will run this function below

    # In our function, we will "return"
    # the HTML that we want flask to serve
def helloWorld():
    return "<h1>This is our flask app!</h1>"