"""
WSGI config for unified_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unified_test.settings")
sys.path.append('/projects/iTec2015Camenita/unified_test/unified_test')
sys.path.append('/projects/iTec2015Camenita/unified_test')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
