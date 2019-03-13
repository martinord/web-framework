# api.py

from webob import Request, Response
from parse import parse
import inspect

class API:
    def __init__(self):
        self.routes = {}
        # dictionary element. Can look as this:
        # {
        #     "/home": <function home at 0x1100a70c8>,
        #     "/about": <function about at 0x1101a80c3>
        # }


    def route(self, path):
        if path in self.routes:
            raise AssertionError("Such route already exists")

        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    def add_route(self, path, handler):
        if path in self.routes:
            raise AssertionError("Such route already exists")

        self.routes[path] = handler


    # Override the call method of the class, called when calling the instances of the class
    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            parse_result = parse(path, request_path) # match the path and the request path. For attributes in the path
            if parse_result is not None:
                return handler, parse_result.named

        return None, None

    def default_response(self, response):
        response.status_code = 404
        response.text = "Not found."

    def handle_request(self, request):
        response = Response()

        # kwargs = keyworded arguments, for example:
        # {
        #     'name': 'Matthew'
        # }

        handler, kwargs = self.find_handler(request_path=request.path)

        if handler is not None:
            if inspect.isclass(handler):
                # class-based handler being used: call the handler depending on request method (get, post...)
                handler = getattr(handler(), request.method.lower(), None)
                if handler is None:
                    raise AttributeError("Method not allowed: ", request.method)
            handler(request, response, **kwargs)
        else:
            self.default_response(response)

        return response
