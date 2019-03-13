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

# Class-based handler
@app.route("/book")
class BooksResource:
    def get(self, req, resp):
        resp.text = "Books page"

# Alternative way to add a routes
def alt(request, response):
    response.text = "This is the alt page"

app.add_route("/alt", alt)

# Template support
@app.route("/template")
def template_handler(req, resp):
    resp.body = app.template("index.html", context={"name":"Web-framework", "title":"My web framework"}).encode()
