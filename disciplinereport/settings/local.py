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
        'ENGINE': env.get("DB_DRIVER", 'django.db.backends.sqlite3'),
        'HOST': env.get("DB_HOST"),
        'NAME': env.get("DB_NAME", os.path.join(VAR_ROOT, 'disciplinereport')),
        'USER': env.get("DB_USER"),
        'PASSWORD': env.get("DB_PASSWORD"),
        'PORT': env.get("DB_PORT"),
     },
}


# print DATABASES