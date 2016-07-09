from disciplinereport.settings.base import *

#==============================================================================
# Generic Django project settings
#==============================================================================
SITE_ID = 2
ALLOWED_HOSTS = ['*']

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
