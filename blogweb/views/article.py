from pyramid.view import view_config

from ..models import DBSession
from ..models.article import Article

@view_config(route_name='article_index', renderer='blogweb:templates/article/index.pt')
def index(request):
    return {}

@view_config(route_name='article_detail', renderer='blogweb:templates/article/detail.pt')
def detail(request):
    article_id = request.matchdict['article_id']
    article = DBSession.query(Article).filter_by(article_id=article_id).first()
    return dict(article=article)
