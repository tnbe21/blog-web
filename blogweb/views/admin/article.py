import transaction

from pyramid.view import view_config

from ...models import DBSession
from ...models.article import Article

@view_config(route_name='admin_articles', renderer='blogweb:templates/admin/articles.pt')
def index(request):
    return {}

@view_config(route_name='admin_article_edit_view', renderer='blogweb:templates/admin/article_edit.pt')
def edit_view(request):
    article_id = request.params.get('article_id')
    article = DBSession.query(Article).filter_by(article_id=article_id).first()
    return dict(article=article)

@view_config(route_name='admin_article_add')
def add(request):
    with transaction.manager:
        new_article = Article()
        new_article.article_id = DBSession.query(Article).count() + 1;
        new_article.title = request.params.get('title')
        new_article.body = request.params.get('body')
        new_article.status = request.params.get('status')
        DBSession.add(new_article)
        return {}

@view_config(route_name='admin_article_edit')
def edit(request):
    with transaction.manager:
        return {}
