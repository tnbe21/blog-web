import unittest

from pyramid import testing

class TestAdminUsersSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ....views.admin import user
        request = testing.DummyRequest()
        info = user.index(request)
        self.assertEqual(info, {})


class TestAdminUserAddSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ....views.admin import user
        request = testing.DummyRequest()
        info = user.add(request)
        self.assertEqual(info, {})


class TestAdminUserEditSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ....views.admin import user
        request = testing.DummyRequest()
        info = user.edit(request)
        self.assertEqual(info, {})
