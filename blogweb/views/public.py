from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import (
    DBSession
    )

@view_config(route_name='home', renderer='blogweb:templates/blog.pt')
def home(request):
    print "hello"
    return {}

@view_config(route_name='article', renderer='blogweb:templates/blog.pt')
def article(request):
    print "hello article"
    return {}