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
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(VAR_ROOT, 'disciplinereport'),
#     },
# }

DATABASES = {
     'default': {
        'ENGINE': env.get("DB_DRIVER"),
        'HOST': env.get("DB_HOST"),
        'NAME': env.get("DB_NAME"),
        'USER': env.get("DB_USER"),
        'PASSWORD': env.get("DB_PASSWORD"),
        'PORT': env.get("DB_PORT"),
     },
}


# print DATABASES