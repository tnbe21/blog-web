from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

@view_config(route_name='admin_login', renderer='blogweb:templates/admin/login.pt')
def login(request):
    return {}

@view_config(route_name='admin_logout')
def logout(request):
    return HTTPFound(location='/rfwt4w3gtibjqhaljgalkjkl30va/admin/login')
