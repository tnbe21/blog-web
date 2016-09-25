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
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)

    config.include('pyramid_chameleon')
    config.include('pyramid_tm')

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('article_index', '/')
    config.add_route('article_detail', '/article/{article_id}')

    config.add_route('article_tag_list', '/article_tag/list')

    config.add_route('admin_login', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/login')
    config.add_route('admin_logout', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/logout')

    config.add_route('admin_article_index', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/article/index')

    config.add_route('admin_article_add_form', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/article/add_form')
    config.add_route('admin_article_add', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/article/add')

    config.add_route('admin_article_edit_form', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/article/edit_form/{article_id}')
    config.add_route('admin_article_edit', '/rfwt4w3gtibjqhaljgalkjkl30va/admin/article/edit')

    config.scan()
    return config.make_wsgi_app()
