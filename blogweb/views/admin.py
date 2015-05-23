from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel
    )

@view_config(route_name='admin_login', renderer='templates/admin/login.pt')
def admin_login(request):
    print "hello admin login"
    return {}

@view_config(route_name='admin_logout', renderer='templates/admin/login.pt')
def admin_logout(request):
    print "hello admin logout"
    return {}

@view_config(route_name='admin_home', renderer='templates/admin/home.pt')
def admin_home(request):
    print "hello admin home"
    return {}

@view_config(route_name='admin_users', renderer='templates/admin/users.pt')
def admin_users(request):
    print "hello admin users"
    return {}

@view_config(route_name='admin_user_add', renderer='templates/admin/user_edit.pt')
def admin_user_add(request):
    print "hello admin user add"
    return {}

@view_config(route_name='admin_user_edit', renderer='templates/admin/user_edit.pt')
def admin_user_edit(request):
    print "hello admin user edit"
    return {}

@view_config(route_name='admin_articles', renderer='templates/admin/articles.pt')
def admin_articles(request):
    print "hello admin articles"
    return {}

@view_config(route_name='admin_article_add', renderer='templates/admin/article_edit.pt')
def admin_article_add(request):
    print "hello admin article add"
    return {}

@view_config(route_name='admin_article_edit', renderer='templates/admin/article_edit.pt')
def admin_article_edit(request):
    print "hello admin article edit"
    return {}

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_blog-web_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

