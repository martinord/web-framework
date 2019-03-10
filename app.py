# app.py

# Idea: create a web framework compatible with WSGI specification
# (Web Server Gateway Interface specification) to use with gunicorn (WSGI python server)

from api import API

app = API()
