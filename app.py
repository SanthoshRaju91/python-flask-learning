from flask import Flask

# __name__ -> This is python telling the application, the modules from package you need to use from
# In flask, it gives a context of where the application is running and to look for files.
app = Flask(__name__)

@app.route("/")
def index():
    return "Index page"

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {name}"

@app.route("/hello/<int:planet>")
def hello_planet(planet):
    return f"Hello, planet #{planet}"
