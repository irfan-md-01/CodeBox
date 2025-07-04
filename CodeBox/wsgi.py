"""
WSGI config for CodeBox project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CodeBox.settings')

application = get_wsgi_application()

# ✅ WhiteNoise AFTER get_wsgi_application()
from whitenoise import WhiteNoise
application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), 'assets'))

