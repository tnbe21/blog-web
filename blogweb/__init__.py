from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base
    )

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind = engine)
    Base.metadata.bind = engine

    config = Configurator(settings = settings)

    config.include('pyramid_chameleon')

    config.add_static_view('static', 'static', cache_max_age = 3600)

    config.add_route('home', '/')
    config.add_route('article', '/article/{id}')

    config.add_route('admin_login', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/login')
    config.add_route('admin_logout', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/logout')
    config.add_route('admin_home', '/rfwt4w3gtibjqhaljgalkjkl30va/admin')

    config.add_route('admin_users', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/users')
    config.add_route('admin_user_add', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/user/add')
    config.add_route('admin_user_edit', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/user/{id}/edit')

    config.add_route('admin_articles', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/articles')
    config.add_route('admin_article_add', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/article/add')
    config.add_route('admin_article_edit', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/article/{id}/edit')

    config.scan()
    return config.make_wsgi_app()
