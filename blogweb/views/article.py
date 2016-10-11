import time
from datetime import datetime

from pyramid.view import view_config

from ..models.article import Article


@view_config(route_name='article_index', renderer='blogweb:templates/article/index.pt')
def index(request):
    LIMIT_PER_PAGE = 3
    page = 0 if request.params.get('page') is None else int(request.params.get('page'))
    from_idx = 0 if request.params.get('page') is None else int(request.params.get('page')) * LIMIT_PER_PAGE
    to_idx = from_idx + LIMIT_PER_PAGE
    tag = request.params.get('tag')
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

    articles = Article().list(from_dt, to_dt, tag, from_idx, to_idx)

    return dict(articles=articles)


@view_config(route_name='article_detail', renderer='blogweb:templates/article/detail.pt')
def detail(request):
    article_id = request.matchdict['article_id']
    article = Article().get(article_id)
    return dict(article=article)


@view_config(route_name='current_title_list', renderer='json')
def current_title_list(request):
    list = Article().current_title_list()
    return [{'id': article.article_id, 'title': article.title} for article in list]


@view_config(route_name='yearly_map', renderer='json')
def yearly_map(request):
    articles = Article().list(None, None, None, 0, None)
    map = {}
    for article in articles:
        create_dt = datetime.fromtimestamp(article.create_dt)
        year = create_dt.strftime('%Y')
        month = create_dt.strftime('%m')
        year_month_key = year + '-' + month
        if not map.has_key(year):
            map[year] = {}
        if not map[year].has_key(year_month_key):
            map[year][year_month_key] = []
        month_list = map[year][year_month_key]
        month_list.append(article.article_id)

    return map
