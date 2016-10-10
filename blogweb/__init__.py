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

    config.add_route('current_title_list', '/current_title_list')
    config.add_route('monthly_map', '/monthly_map')
    config.add_route('tag_list', '/tag/list')

    admin_root_path = '/%s/admin' % settings['admin.root_path']
    print('admin_root_path: %s' % admin_root_path)
    config.add_route('admin_login', '%s/login' % admin_root_path)
    config.add_route('admin_logout', '%s/logout' % admin_root_path)

    config.add_route('admin_article_index', '%s/admin/article/index' % admin_root_path)

    config.add_route('admin_article_add_form', '%s/article/add_form' % admin_root_path)
    config.add_route('admin_article_add', '%s/article/add' % admin_root_path)

    config.add_route('admin_article_edit_form', '%s/article/edit_form/{article_id}' % admin_root_path)
    config.add_route('admin_article_edit', '%s/article/edit' % admin_root_path)

    config.scan()
    return config.make_wsgi_app()
