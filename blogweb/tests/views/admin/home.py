import unittest

from pyramid import testing


class TestAdminHomeSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ....views.admin import home
        request = testing.DummyRequest()
        info = home.home(request)
        self.assertEqual(info, {})


class TestAdminLoginSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ....views.admin import home
        request = testing.DummyRequest()
        info = home.login(request)
        self.assertEqual(info, {})


class TestAdminLogoutSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ....views.admin import home
        request = testing.DummyRequest()
        info = home.logout(request)
        self.assertEqual(info, {})
