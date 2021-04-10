
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,  render_template

app = Flask(__name__)

@app.route('/Hello')
def hello_world():
    return 'Hello from Flask!'


@app.route("/")
def home():
    return render_template("index.html")



