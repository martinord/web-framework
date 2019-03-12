# test_web-framework.copyright
import pytest

from api import API

@pytest.fixture
def api():
    return API()

def test_basic_route(api):
    @api.route("/home")
    def home(request, response):
        response.text = "FOO"

    with pytest.raises(AssertionError):
        @api.route("/home")
        def home2(request, response):
            response.text = "FOO"
