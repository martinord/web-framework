# api.py

class API:
    # Override the call method of the class, called when calling the instances of the class
    def __call__(self, environ, start_response):
        # The 'b' in front of a string indicates that those are converted to bytes
        response_body = b"Hello, world!"
        status = "200 OK"
        start_response(status, headers=[])
        return iter([response_body])
