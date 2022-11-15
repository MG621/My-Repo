from flask import Flask
from flask import render_template

# Create the app
app = Flask(__name__)

def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

# Create a homepage for the app
@app.route("/")
# When we go to our.URL.com/
    # Then flask will run this function below
def base():
    details = readDetails('static/thing.txt')
    return render_template('base.html', aboutMe=details)


    # In our function, we will "return" 
    # the HTML that we want flask to serve
@app.route("/other/")
# When we go to our.URL.com/
    # Then flask will run this function below
def base1():
    details = readDetails('static/thing.txt')
    return render_template('other.html', aboutMe=details)
