# api.py

from webob import Request, Response

class API:
    # Override the call method of the class, called when calling the instances of the class
    def __call__(self, environ, start_response):
        request = Request(environ)

        response = Response()
        response.text = "Hello World!"

        return response(environ, start_response)
