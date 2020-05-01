import pytest
from tests.conftest import app, client
from myapp import create_app


def test_config(app):
    assert create_app().config['TESTING'] == False
    assert app().config['TESTING'] == True
    assert app().config['CSRF_ENABLED'] == False

def test_hello(app, client):
    assert 200 == client.get('/').status_code
    assert b'Hello world' in client.get('/').data