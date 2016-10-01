from pyramid.view import view_config

from ..models.articletag import ArticleTag


@view_config(route_name='tag_list', renderer='json')
def list(request):
    tag_list = ArticleTag().list()
    return [{'name': tag.name, 'articleCount': tag.article_count} for tag in tag_list]
