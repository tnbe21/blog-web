import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    Base,
)

# import models you want to initialize (at DB)
from ..models.adminuser import AdminUser
from ..models.article import Article
from ..models.articletag import ArticleTag


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> <initial_admin_user_passwd> [var=value]\n'
          '(example: "%s development.ini passwd")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 3:
        usage(argv)
    config_uri = argv[1]
    initial_admin_user_pass = argv[2]
    options = parse_vars(argv[3:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        DBSession.add(AdminUser('tanabe_taichi', initial_admin_user_pass))
