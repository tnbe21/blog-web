Getting Started
---------------

with
* Python 2.7.10 (installing virtualenv)
* Pyramid 1.7b2
* MySQL 5.6

First,

1. `cd $BLOG-WEB_ROOT`
2. `(virtualenv --no-site-packages $VENV && . $VENV/bin/activate)`
3. `$VENV/bin/easy_install pyramid`
4. `$VENV/bin/python setup.py ${env}`
5. `$VENV/bin/initialize_blog-web_db ${envMode}.ini`
6. `$VENV/bin/pserve ${envMode}.ini`

From the second time,

1. `cd $BLOG-WEB_ROOT`
2. `sh start.sh ${envMode} ${pass}`
