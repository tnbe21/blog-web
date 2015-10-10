from pyramid.view import view_config

@view_config(route_name='article_index', renderer='blogweb:templates/article/index.pt')
def index(request):
    return {}

@view_config(route_name='article_detail', renderer='blogweb:templates/article/detail.pt')
def detail(request):
    return {}
