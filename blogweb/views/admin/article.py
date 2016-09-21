import time
from datetime import datetime

import transaction

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from ...models import DBSession
from ...models.article import Article


@view_config(route_name='admin_article_index', renderer='blogweb:templates/admin/article/index.pt')
def index(request):
    page = request.params.get('page')
    tag = request.params.get('tag')
    year = request.params.get('year')
    month = request.params.get('month')
    return {}


@view_config(route_name='admin_article_add_form', renderer='blogweb:templates/admin/article/add.pt')
def add_form(request):
    return {}


@view_config(route_name='admin_article_add')
def add(request):
    with transaction.manager:
        article = Article()
        article.article_id = DBSession.query(Article).count() + 1
        article.title = request.params.get('title')
        article.body = request.params.get('body')
        article.status = request.params.get('status')
        DBSession.add(article)
        return HTTPFound(location='/rfwt4w3gtibjqhaljgalkjkl30va/admin/article/index')


@view_config(route_name='admin_article_edit_form', renderer='blogweb:templates/admin/article/edit.pt')
def edit_form(request):
    article_id = request.matchdict['article_id']
    article = DBSession.query(Article).filter_by(article_id=article_id).first()
    return dict(article=article)


@view_config(route_name='admin_article_edit')
def edit(request):
    with transaction.manager:
        article_id = request.params.get('article_id')
        article = DBSession.query(Article).filter_by(article_id=article_id).first()
        article.title = request.params.get('title')
        article.body = request.params.get('body')
        article.status = request.params.get('status')
        article.update_dt = int(time.mktime(datetime.now().timetuple()))
        DBSession.add(article)
        return HTTPFound(location='/rfwt4w3gtibjqhaljgalkjkl30va/admin/article/index')
