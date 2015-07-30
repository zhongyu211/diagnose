# filename:mysite.apache.django.wsgi
#!/usr/bin/python
import os, sys
#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
#if path not in sys.path:
#    sys.path.insert(0,'
sys.path.append('/home/alzhong/project/diagnose')
os.environ['DJANGO_SETTINGS_MODULE'] = 'diagnose.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#django.core.handlers.wsgi.WSGIHandler()
