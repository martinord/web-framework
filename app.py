# app.py

# Idea: create a web framework compatible with WSGI specification
def app(environ, start_response):
    # The 'b' in front of a string indicates that those are converted to bytes
    response_body = b"Hello, world!"
    status = "200 OK"
    start_response(status, headers=[])
    return iter([response_body])
