# api.py

from webob import Request, Response

class API:
    # Override the call method of the class, called when calling the instances of the class
    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def handle_request(self, request):
        user_agent = request.environ.get("HTTP_USER_AGENT", "No User Agent Found")

        response = Response()
        response.text = f"Hello, my friend with this user agent: {user_agent}"

        return response
