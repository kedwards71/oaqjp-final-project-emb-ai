"""
Executing this function initiates the Emotion Detection application
on the Flask Channel and deployed on localhost:5000
"""

from flask import Flask, render_template, request

app = Flask("Emotion Detection")



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)