import pytest


@pytest.fixture(scope="class")
def setup():
    print("The first execution")
    yield
    print("the last execution")