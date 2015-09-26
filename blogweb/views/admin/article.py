from pyramid.view import view_config

@view_config(route_name='admin_articles', renderer='blogweb:templates/admin/articles.pt')
def index(request):
    return {}

@view_config(route_name='admin_article_add', renderer='blogweb:templates/admin/article_edit.pt')
def add(request):
    return {}

@view_config(route_name='admin_article_edit', renderer='blogweb:templates/admin/article_edit.pt')
def edit(request):
    return {}
