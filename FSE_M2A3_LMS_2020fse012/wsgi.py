"""
WSGI config for FSE_M2A3_LMS_2020fse012 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FSE_M2A3_LMS_2020fse012.settings')

application = get_wsgi_application()
