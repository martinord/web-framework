# app.py

# Idea: create a web framework compatible with WSGI specification
# (Web Server Gateway Interface specification) to use with gunicorn (WSGI python server)

from api import API

app = API()

# @ symbol establishes a decorator
# In this case gets the app object (instance of API)
# and calls the method "route", adding the next function
# as handler of the path

@app.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page"

@app.route("/about")
def about(request, response):
    response.text = "Hello from the ABOUT page"

# Note: name argument in greeting, is passed as keyworded arguments
@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"
