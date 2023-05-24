import pytest

from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")



class TestDemo(BaseClass):

    def test_fixture_demo(self):
        print("The second execution")

    def test_fixture_demo1(self):
        print("The third execution")

    def test_fixture_demo2(self):
        print("The forth execution")

    def test_fixture_demo3(self):
        print("The fifth execution")

    def test_fixture_demo4(self):
        print("The sixth execution")



