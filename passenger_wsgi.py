import sys, os
cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/quack')  #You must add your project here

sys.path.insert(0,cwd+'/env/bin')
sys.path.insert(0,cwd+'/env/lib/python2.7/site-packages/django')
sys.path.insert(0,cwd+'/env/lib/python2.7/site-packages')

from quack_environment import QUACK_MYSQL_PASSWORD
os.environ['QUACK_MYSQL_PASSWORD'] = QUACK_MYSQL_PASSWORD
os.system('printenv')

os.environ['DJANGO_SETTINGS_MODULE'] = "quack.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
