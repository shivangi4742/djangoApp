"""
WSGI config for rbl_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# add the hellodjango project path into the sys.path
sys.path.append('/rbl_backend/rbl_backend')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/env/Lib/site-packages')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rbl_backend.settings')

application = get_wsgi_application()
