import unittest

from pyramid import testing

class TestArticleIndexSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ...views import article
        request = testing.DummyRequest()
        info = article.index(request)
        self.assertEqual(info, {})


class TestArticleDetailSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ...views import article
        request = testing.DummyRequest()
