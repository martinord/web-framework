# api.py

from webob import Request, Response

class API:
    def __init__(self):
        self.routes = {}
        # dictionary element. Can look as this:
        # {
        #     "/home": <function home at 0x1100a70c8>,
        #     "/about": <function about at 0x1101a80c3>
        # }


    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    # Override the call method of the class, called when calling the instances of the class
    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def handle_request(self, request):
        response = Response()

        for path, handler in self.routes.items():
            if path == request.path:
                handler(request, response)
                return response

        return response
