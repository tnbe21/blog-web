from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)

    config.include('pyramid_chameleon')

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('article', '/article/{id}')

    config.add_route('admin_login', '/ffefer30vaslfsflvalfje/admin/login')
    config.add_route('admin_logout', '/ffefer30vaslfsflvalfje/admin/logout')
    config.add_route('admin_home', '/ffefer30vaslfsflvalfje/admin')

    config.add_route('admin_users', '/ffefer30vaslfsflvalfje/admin/users')
    config.add_route('admin_user_edit', '/ffefer30vaslfsflvalfje/admin/user/{id}/edit')
    config.add_route('admin_user_add', '/ffefer30vaslfsflvalfje/admin/user/add')

    config.add_route('admin_articles', '/ffefer30vaslfsflvalfje/admin/articles')
    config.add_route('admin_article_edit', '/ffefer30vaslfsflvalfje/admin/article/{id}/edit')
    config.add_route('admin_article_add', '/ffefer30vaslfsflvalfje/admin/article/add')

    config.scan()
    return config.make_wsgi_app()
