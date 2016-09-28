from pyramid.view import view_config

from ..models.tag import Tag


@view_config(route_name='tag_list', renderer='json')
def list(request):
    tags = Tag().list()
    return tags
