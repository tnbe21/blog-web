from pyramid.view import view_config

@view_config(route_name='home', renderer='blogweb:templates/blog.pt')
def home(request):
    return {}

@view_config(route_name='article', renderer='blogweb:templates/blog.pt')
def article(request):
    return {}
