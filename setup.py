import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()

requires = [
    'pyramid == 1.7b2',
    'pyramid_chameleon == 0.3',
    'pyramid_debugtoolbar == 3.0',
    'pyramid_tm == 0.12.1',
    'SQLAlchemy == 1.0.12',
    'transaction == 1.5.0',
    'zope.sqlalchemy == 0.7.6',
    'waitress == 0.9.0',
    'mysql-python == 1.2.5'
]

setup(name='blog-web',
      version='0.0',
      description='blog-web',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='tnbe21',
      author_email='',
      url='http://tnbe21.com',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='blogweb',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = blogweb:main
      [console_scripts]
      initialize_blog-web_db = blogweb.scripts.initializedb:main
      """,
      )
