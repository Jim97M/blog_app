#This is the configuration to run your project as a web server
#Gateway Interface (WSGI) application
#

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

application = get_wsgi_application()
