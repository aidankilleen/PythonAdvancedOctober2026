# app.py
# flask web application demo

import os
import sys
from flask import Flask, render_template

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from UserDAO import UserDAO

app = Flask(__name__)


@app.route("/")
def home():
    names = ["Alice", "Bob", "Carol", "Dan"]


    return render_template("home.html", 
                           name="Aidan", 
                           team=names)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/members")
def member():
    dao = UserDAO()

    members = dao.get_all()

    return render_template("members.html", members=members)

if __name__ == "__main__":
    app.run(debug=True)


