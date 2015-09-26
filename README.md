Getting Started
---------------

with
* Python 2.7.10 (installing virtualenv)
* MySQL 5.6

1. `cd $BLOG-WEB_ROOT`
2. `(virtualenv --no-site-packages env && . env/bin/activate)`
3. `$VENV/bin/easy_install pyramid`
4. `$VENV/bin/python setup.py develop`
5. `$VENV/bin/initialize_blog-web_db development.ini`
6. `$VENV/bin/pserve development.ini`
