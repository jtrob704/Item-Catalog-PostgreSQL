import sys
sys.path.insert(0, '/var/www/html/')
sys.path.append('/home/jtr/.local/lib/python2.7/site-packages')

from application import app as application

application.secret_key = 'itemCatalog#91'
application.config['SESSION_TYPE'] = 'filesystem'
application.config['sqlalchemy'] = 'postgresql://catalog:catalog@localhost:5432/ \
                                    items'
