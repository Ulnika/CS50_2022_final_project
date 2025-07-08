import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from forms import ContactForm
import pandas as pd


# Configure application
app = Flask(__name__)
app.secret_key = 'secretKey'


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/places")
def places():
    return render_template("places.html")

@app.route('/contact', methods=["GET","POST"])
def get_contact():
    form = ContactForm()

    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        res.to_csv('./contactusMessage.csv')
        return redirect("contactsaved")
        print("The data are saved !")

    else:
        return render_template("contact.html", form=form)

@app.route("/Hallstadt")
def Hallstadt():
    return render_template("Hallstadt.html")

@app.route("/Carpathian")
def Carpathian():
    return render_template("Carpathian.html")

@app.route("/Schilthorn")
def Schilthorn():
    return render_template("Schilthorn.html")

@app.route("/Neuschwanstein")
def Neuschwanstein():
    return render_template("Neuschwanstein.html")

@app.route("/contactsaved")
def contactsaved():
    return render_template("contactsaved.html")

