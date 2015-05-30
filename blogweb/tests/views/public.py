import unittest
import transaction

from pyramid import testing

from ...models import DBSession

class TestHomeSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from ...models import (
            Base,
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_passing_view(self):
        from ...views import public
        request = testing.DummyRequest()
        info = public.home(request)
        self.assertEqual(info, {})

class TestArticleSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from ...models import (
            Base,
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_passing_view(self):
        from ...views import public
        request = testing.DummyRequest()
        info = public.article(request)
        self.assertEqual(info, {})
