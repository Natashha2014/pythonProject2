#what is a pytest --- pytest is a testing fraimwork that is desinged to automate the project this framework is also used
#to perform unit testing. menaing developers also used this framework to perform unit testing. pytestworks only with python
#pytest is very reach with lot of different methods such as fixtures and marks.
#pytest and unit test is very popular it is almos same but pytest introduced later and because readebility pytest
import pytest

from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestFixtureDemo(BaseClass):
    def test_(self):
        weather = 9
        if weather < 10:
            print("cold")
        else:
            print("beautiful")

    def test_greeting(self):
        message = "Hello world"
        assert "Hello" in message, "The provided string is not matching the message"
        print("The test has passed")






