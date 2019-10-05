import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    name = request.form.get("name")
    role = request.form.get("role")
    club = request.form.get("club")

    if not name or not role or not club:
        return render_template("error.html", message="You need to provide information about Name, Role and/or Club")

    file = open("survey.csv", "a")
    writer = csv.writer(file)
    writer.writerow((name, club, role))
    file.close()
    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    try:
        file = open("survey.csv", "r")
        reader = csv.reader(file)
        result = list(reader)
        return render_template("registered.html", result=result)

    except FileNotFoundError:
        return render_template("error.html", message="File Could not be found")

