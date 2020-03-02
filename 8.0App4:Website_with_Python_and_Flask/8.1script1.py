""" Import the class(Flask) of library(flask) """
from flask import Flask

# create a flask obj instance
app = Flask(__name__)

# create a decorator with url where yu'll view the website
@app.route('/')
def home():
    return "Home content goes here!"

@app.route('/about/')
def about():
    return "About content goes here!"

if __name__ == "__main__":
    app.run(debug=True)

# Run script and open web at "http://127.0.0.1:5000/"