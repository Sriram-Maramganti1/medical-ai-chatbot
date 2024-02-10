from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('here2help.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = 