from pyramid.view import view_config

from ..models.articletag import ArticleTag


@view_config(route_name='tag_list', renderer='json')
def list(request):
    tags = ArticleTag().list()
    return tags
