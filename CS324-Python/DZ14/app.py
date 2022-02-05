from flask import Flask, render_template
from datetime import datetime

contacts = [
    {
        "name": "Stefan",
        "age": "20",
        "email": "mymail@gmail.com"
    }
]

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home_page():
    return render_template("index.html", title="Home Page")

@app.route("/about")
def about_page():
    return render_template("about.html", title="About Page", date=datetime.now())

@app.route("/contact")
def contact_page():
    return render_template("contact.html", title="Contact Page", contacts=contacts)