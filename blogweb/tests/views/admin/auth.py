import unittest

from pyramid import testing
from pyramid.httpexceptions import HTTPFound


class TestAdminLoginSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ....views.admin import auth
        request = testing.DummyRequest()
        info = auth.login(request)
        self.assertEqual(info, {})


class TestAdminLogoutSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ....views.admin import auth
        request = testing.DummyRequest()
        info = auth.logout(request)
