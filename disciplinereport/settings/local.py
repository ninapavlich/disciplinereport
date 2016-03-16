from disciplinereport.settings.base import *

#==============================================================================
# Generic Django project settings
#==============================================================================


DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']

#==============================================================================
# LOCAL DATBASE
#==============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'disciplinereport'),
    },
}
