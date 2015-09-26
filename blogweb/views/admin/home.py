from pyramid.view import view_config

@view_config(route_name='admin_home', renderer='blogweb:templates/admin/home.pt')
def home(request):
    return {}

@view_config(route_name='admin_login', renderer='blogweb:templates/admin/login.pt')
def login(request):
    return {}

@view_config(route_name='admin_logout', renderer='blogweb:templates/admin/login.pt')
def logout(request):
    return {}
