from pyramid.view import view_config

from ..models import DBSession
from ..models.article import Article

@view_config(route_name='article_index', renderer='blogweb:templates/article/index.pt')
def index(request):
    limit_per_page = int(request.registry.settings['limit_per_page'])
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

    if from_dt > 0 and to_dt > 0:
        create_dt_filter_query = "create_dt >= %d and create_dt <= %d" % (from_dt, to_dt)
        article = DBSession.query(Article).filter(create_dt_filter_query).order_by(Article.article_id.desc())[page:(page + limit_per_page - 1)]
    else:
        article = DBSession.query(Article).order_by(Article.article_id.desc())[page:(page + limit_per_page - 1)]

    return {}

@view_config(route_name='article_detail', renderer='blogweb:templates/article/detail.pt')
def detail(request):
    article_id = request.matchdict['article_id']
    article = DBSession.query(Article).filter_by(article_id=article_id).first()
    return dict(article=article)
