import unittest

from pyramid import testing

class TestHomeSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ...views import public
        request = testing.DummyRequest()
        info = public.home(request)
        self.assertEqual(info, {})


class TestArticleSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ...views import public
        request = testing.DummyRequest()
        info = public.article(request)
        self.assertEqual(info, {})
