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
    if request.params.get('year') is not None:
        year = int(request.params.get('year'))
        if request.params.get('month') is not None:
            month = int(request.params.get('month'))
            from_dt = int(time.mktime(datetime(year=year, month=month, day=1)))
            to_dt = int(time.mktime(datetime(year=year, month=month + 1, day=1))) - 1
        else:
            from_dt = int(time.mktime(datetime(year=year, month=1, day=1)))
            to_dt = int(time.mktime(datetime(year=year + 1, month=1, day=1))) - 1

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


@view_config(route_name='archive_maps', renderer='json')
def archive_maps(request):
    articles = Article().list(None, None, None, None, None)
    map = {}
    for article in articles:
        create_dt = datetime.fromtimestamp(article.create_dt)
        year = create_dt.strftime('%Y')
        month = create_dt.strftime('%m')
        year_month_key = year + '-' + month
        if not map.has_key(year):
            map[year] = {}
        if not map[year].has_key(month):
            map[year][month] = 0
        map[year][month] += 1

    return map
