import time
from datetime import datetime

from pyramid.view import view_config

from ..models.article import Article


@view_config(route_name='article_index', renderer='blogweb:templates/article/index.pt')
def index(request):
    page = 0 if request.params.get('page') is None else int(request.params.get('page'))
    tag = '' if request.params.get('tag') is None else request.params.get('get')
    year = request.params.get('year')
    month = request.params.get('month')
    from_dt = 0
    to_dt = 0
    if year is not None:
        if month is not None:
            from_dt = int(time.mktime(datetime.datetime(year, month, 1)))
            to_dt = int(datetime.datetime(year, month + 1, 1)) - 1
        else:
            from_dt = int(time.mktime(datetime.datetime(year, 1, 1)))
            to_dt = int(datetime.datetime(year + 1, 1, 1)) - 1

    articles = Article().list(from_dt, to_dt, tag, page)

    return dict(articles=articles)


@view_config(route_name='article_detail', renderer='blogweb:templates/article/detail.pt')
def detail(request):
    article_id = request.matchdict['article_id']
    article = Article().get(article_id)
    return dict(article=article)


@view_config(route_name='current_title_list', renderer='json')
def current_title_list(request):
    return Article().current_title_list()
