from webtest.app import TestRequest
from horseman.http import Cookies


def test_request_parse_cookies():

    # A simple cookie
    request = TestRequest(environ={}, cookies={'key': 'value'})
    cookies = Cookies.from_environ(request.environ)
    assert cookies['key'] == 'value'

    # No cookie
    request = TestRequest(environ={})
    cookies = Cookies.from_environ(request.environ)
    assert not cookies
