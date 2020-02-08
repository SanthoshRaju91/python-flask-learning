from flask import Flask, render_template, request, redirect, url_for

# __name__ -> This is python telling the application, the modules from package you need to use from
# In flask, it gives a context of where the application is running and to look for files.
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/<name>")
def hello_name(name):
    return render_template("hello/name.html", t_name=name)

@app.route("/hello/<int:planet>")
def hello_planet(planet):
    return render_template("hello/planet.html", t_planet=planet)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        return redirect(url_for("registered"))
    return render_template("form.html")

@app.route("/thank-you")
def registered():
    return "Thank you for registering."
