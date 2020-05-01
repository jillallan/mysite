import os
import pytest

from myapp import create_app
from config import TestingConfig

@pytest.fixture
def app():
    app = create_app()
    app.config.from_object(TestingConfig)

    context = app.app_context()
    context.push()

    yield app

    context.pop()

@pytest.fixture
def client(app):
    return app.test_client()


