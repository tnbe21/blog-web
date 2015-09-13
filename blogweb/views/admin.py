from pyramid.view import view_config

from ..models.adminuser import AdminUser
from ..models.article import Article


@view_config(route_name='admin_login', renderer='blogweb:templates/admin/login.pt')
def admin_login(request):
    return {}

@view_config(route_name='admin_logout', renderer='blogweb:templates/admin/login.pt')
def admin_logout(request):
    return {}

@view_config(route_name='admin_home', renderer='blogweb:templates/admin/home.pt')
def admin_home(request):
    return {}

@view_config(route_name='admin_users', renderer='blogweb:templates/admin/users.pt')
def admin_users(request):
    return {}

@view_config(route_name='admin_user_add', renderer='blogweb:templates/admin/user_edit.pt')
def admin_user_add(request):
    return {}

@view_config(route_name='admin_user_edit', renderer='blogweb:templates/admin/user_edit.pt')
def admin_user_edit(request):
    return {}

@view_config(route_name='admin_articles', renderer='blogweb:templates/admin/articles.pt')
def admin_articles(request):
    return {}

@view_config(route_name='admin_article_add', renderer='blogweb:templates/admin/article_edit.pt')
def admin_article_add(request):
    return {}

@view_config(route_name='admin_article_edit', renderer='blogweb:templates/admin/article_edit.pt')
def admin_article_edit(request):
    return {}
