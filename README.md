# Web framework in Python
This is a web framework written in Python for backend purposes, compatible with WSGI specification. The objective is to get used to Python and to learn backend technologies.
It is based in the [article](http://rahmonov.me/posts/write-python-framework-part-one/) published by [Rahmonov](http://rahmonov.me/).

## Starting environment
* Init a virtual environment (`python3.6 venv venv`) and start it with `source venv/bin/activate`
* Create app.py
* `pip install gunicorn`
* `gunicorn app:app` (start the server gunicorn)
* Browse http://localhost:8000

## Packages used
* gunicorn
* webob
* parse
