from pyramid.view import view_config

@view_config(route_name='admin_users', renderer='blogweb:templates/admin/users.pt')
def index(request):
    return {}

@view_config(route_name='admin_user_add', renderer='blogweb:templates/admin/user_edit.pt')
def add(request):
    return {}

@view_config(route_name='admin_user_edit', renderer='blogweb:templates/admin/user_edit.pt')
def edit(request):
    return {}
