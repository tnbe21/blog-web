import unittest
import transaction

from pyramid import testing
from ...models.article import Article


def _initTestingDB():
    from sqlalchemy import create_engine
    from ...models import Base, DBSession

    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
    DBSession.configure(bind=engine)
    with transaction.manager:
        model = Article()
        model.article_id = 1
        model.title = 'firstArticle'
        model.body = 'This is the first article.'
        model.status = 1
        DBSession.add(model)
    return DBSession


class TestArticleIndexSuccessCondition(unittest.TestCase):

    def setUp(self):
        self.session = _initTestingDB()
        self.config = testing.setUp()

    def tearDown(self):
        self.session.remove()
        testing.tearDown()

    def test_passing_view(self):
        from ...views import article
        request = testing.DummyRequest()
        list = article.index(request)
        self.assertEqual(len(list['articles']), 1)


class TestArticleDetailSuccessCondition(unittest.TestCase):

    def setUp(self):
        self.session = _initTestingDB()
        self.config = testing.setUp()

    def tearDown(self):
        self.session.remove()
        testing.tearDown()

    def test_passing_view(self):
        from ...views import article
        request = testing.DummyRequest()
        request.matchdict['article_id'] = 1
        detail = article.detail(request)
        self.assertEqual(detail['article'].title, 'firstArticle')
