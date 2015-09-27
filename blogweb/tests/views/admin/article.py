import unittest

from pyramid import testing

class TestAdminArticlesSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ....views.admin import article
        request = testing.DummyRequest()
        info = article.index(request)
        self.assertEqual(info, {})


class TestAdminArticleEditViewSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ....views.admin import article
        request = testing.DummyRequest()


class TestAdminArticleAddSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ....views.admin import article
        request = testing.DummyRequest()


class TestAdminArticleEditSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_view(self):
        from ....views.admin import article
        request = testing.DummyRequest()
