from pyramid.view import view_config

from ..models import (
    DBSession
    )


@view_config(route_name='admin_login', renderer='blogweb:templates/admin/login.pt')
def admin_login(request):
    print "hello admin login"
    return {}

@view_config(route_name='admin_logout', renderer='blogweb:templates/admin/login.pt')
def admin_logout(request):
    print "hello admin logout"
    return {}

@view_config(route_name='admin_home', renderer='blogweb:templates/admin/home.pt')
def admin_home(request):
    print "hello admin home"
    return {}

@view_config(route_name='admin_users', renderer='blogweb:templates/admin/users.pt')
def admin_users(request):
    print "hello admin users"
    return {}

@view_config(route_name='admin_user_add', renderer='blogweb:templates/admin/user_edit.pt')
def admin_user_add(request):
    print "hello admin user add"
    return {}

@view_config(route_name='admin_user_edit', renderer='blogweb:templates/admin/user_edit.pt')
def admin_user_edit(request):
    print "hello admin user edit"
    return {}

@view_config(route_name='admin_articles', renderer='blogweb:templates/admin/articles.pt')
def admin_articles(request):
    print "hello admin articles"
    return {}

@view_config(route_name='admin_article_add', renderer='blogweb:templates/admin/article_edit.pt')
def admin_article_add(request):
    print "hello admin article add"
    return {}

@view_config(route_name='admin_article_edit', renderer='blogweb:templates/admin/article_edit.pt')
def admin_article_edit(request):
    print "hello admin article edit"
    return {}
