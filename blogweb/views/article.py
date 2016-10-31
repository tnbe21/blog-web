import time
from datetime import datetime

from pyramid.view import view_config

from ..models.article import Article


@view_config(route_name='article_index', renderer='blogweb:templates/article/index.pt')
def index(request):
    LIMIT_PER_PAGE = 3
    from_idx = 0 if request.params.get('page') is None else int(request.params.get('page')) * LIMIT_PER_PAGE
    to_idx = from_idx + LIMIT_PER_PAGE
    tag = request.params.get('tag')
    from_dt = 0
    to_dt = 0
    if request.params.get('year') is not None:
        year = int(request.params.get('year'))
        if request.params.get('month') is not None:
            month = int(request.params.get('month'))
            from_dt = int(time.mktime(datetime(year, month, 1).timetuple()))
            to_dt = int(time.mktime(datetime(year, month + 1, 1).timetuple())) - 1
        else:
            from_dt = int(time.mktime(datetime(year, 1, 1).timetuple()))
            to_dt = int(time.mktime(datetime(year + 1, 1, 1).timetuple())) - 1

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


@view_config(route_name='archive_list', renderer='json')
def archive_list(request):
    create_dt_list = Article().all_create_dt_list()
    list = []
    for e in create_dt_list:
        create_dt = datetime.fromtimestamp(e.create_dt)
        year = create_dt.strftime('%Y')
        month = create_dt.strftime('%m')

        temp_yearly = None
        for yearly in list:
            if yearly is not None and year is yearly['year']:
                temp_yearly = yearly
        if temp_yearly is None:
            temp_yearly = {}
            temp_yearly['year'] = year
            temp_yearly['monthlyList'] = []
            list.append(temp_yearly)

        temp_monthly = None
        for monthly in temp_yearly['monthlyList']:
            if monthly is not None and month is monthly['month']:
                temp_monthly = monthly
        if temp_monthly is None:
            temp_monthly = {}
            temp_monthly['month'] = month
            temp_monthly['count'] = 1
            temp_yearly['monthlyList'].append(temp_monthly)
        else:
            temp_monthly['count'] += 1

    return list
