# [Web framework in Python](https://github.com/martinord/web-framework)
This is a web framework written in Python for backend purposes, compatible with WSGI specification. The objective is to get used to Python and to learn backend technologies.

It is based in the [article](http://rahmonov.me/posts/write-python-framework-part-one/) published by [Rahmonov](http://rahmonov.me/).

The repo of Rahmanov can be also found [here](https://github.com/rahmonov/alcazar).

## Starting environment
* Init a virtual environment (`python3.6 venv venv`) and start it with `source venv/bin/activate`
* `pip install gunicorn`
* `gunicorn app:app` (start the server gunicorn)
* Browse http://localhost:8000

### Packages used
* gunicorn
* webob
* parse
* pytest
* Jinja2

### Unit testing
Run `pytest test_web-framework.py` to run the unit thesting.

## Licence

Source code can be found on [github](https://github.com/martinord/web-framework), licenced under [MIT](http://opensource.org/licenses/mit-license.php).

Developed by [Martiño Rivera](https://github.com/martinord)
