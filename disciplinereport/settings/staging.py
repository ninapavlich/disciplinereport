from disciplinereport.settings.base import *

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = env.get("DEBUG", False)
TEMPLATE_DEBUG = DEBUG
HTML_MINIFY = DEBUG==False

TEMPLATE_DEBUG = DEBUG
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