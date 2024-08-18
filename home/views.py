from . import Home
from flask import render_template

def views():
    @Home.route("/")
    def index():
        return render_template("home.html")

    return Home
