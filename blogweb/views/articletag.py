from pyramid.view import view_config

from ..models import DBSession
from ..models.articletag import ArticleTag


@view_config(route_name='article_tag_list', renderer='json')
def list(request):
    articleTags = DBSession.query(ArticleTag)
    return {'tags': articleTags}
