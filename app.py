from flask import Flask, render_template, request, redirect, url_for
import os
import smtplib

app = Flask(__name__)




@app.route('/')
def home_page():
    return render_template("index.html")  




@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")  


if __name__ == '__main__':
    app.run(debug=True)