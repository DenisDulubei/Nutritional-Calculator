import pytest
from resources.login import Login


class TestShare:

    def test_login(self, browser):
        login = Login(browser)
        login.access()
