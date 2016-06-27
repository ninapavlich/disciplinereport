import os
import sys
import copy
import herokuify

from django.conf.global_settings import *   # pylint: disable=W0614,W0401

from disciplinereport import env
import disciplinereport as project_module

# -- Server settings
if os.environ.get( 'ENVIRONMENT', 'local' ) != 'local':
    if env.get("IS_ON_HEROKU", False):
        IS_ON_SERVER = True
        IS_ON_HEROKU = True
    else:
        IS_ON_SERVER = True
        IS_ON_HEROKU = False
else:
    IS_ON_SERVER = False
    IS_ON_HEROKU = False


if os.environ.get( 'ENVIRONMENT', 'local' ) == 'heroku':
    
    # USE_SSL = True
    # SSL_PATHS = [r'/*']
    # SESSION_COOKIE_SECURE = True
    USE_SSL = False    
    SSL_PATHS = []

else:
    USE_SSL = False    
    SSL_PATHS = []

#==============================================================================
# Calculation of directories relative to the project module location
#==============================================================================

APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir))
DATA_DIR = os.path.join(APP_DIR, 'data')
LIBS_DIR = os.path.join(APP_DIR, 'libs')
PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))
PYTHON_BIN = os.path.dirname(sys.executable)
ve_path = os.path.dirname(os.path.dirname(os.path.dirname(PROJECT_DIR)))

if os.path.exists(os.path.join(PYTHON_BIN, 'activate_this.py')):
    VAR_ROOT = os.path.join(os.path.dirname(PYTHON_BIN), 'var')
elif ve_path and os.path.exists(os.path.join(ve_path, 'bin',
        'activate_this.py')):
    VAR_ROOT = os.path.join(ve_path, 'var')
else:
    VAR_ROOT = os.path.join(PROJECT_DIR, 'var')

if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

#==============================================================================
# Add libs
#==============================================================================

sys.path.append(LIBS_DIR)

if IS_ON_SERVER:
    if IS_ON_HEROKU:
        VENV_SRC_DIR = os.path.join(APP_DIR, '.heroku', 'src')        
        VENV_LIB_DIR = os.path.join(APP_DIR, '.heroku') #TODO    
    else:
        VENV_SRC_DIR = os.path.join(APP_DIR, os.pardir)
        VENV_LIB_DIR = os.path.join(APP_DIR, os.pardir, os.pardir, 'lib', 'python2.7', 'site-packages') #TODO
else:
    VENV_SRC_DIR = os.path.join(APP_DIR, 'venv', 'src')
    VENV_LIB_DIR = os.path.join(APP_DIR, 'venv', 'python2.7', 'site-packages')


#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = env.get("DEBUG", True)
TEMPLATE_DEBUG = DEBUG
HTML_MINIFY = DEBUG==False

SITE_TITLE = 'Discipline Report'
SITE_DESCRIPTION = 'Website'
GRAPPELLI_ADMIN_TITLE = SITE_TITLE
GRAPPELLI_INDEX_DASHBOARD = 'disciplinereport.apps.core.dashboard.AdminDashboard'

SITE_ID = int(env.get("SITE_ID", 1))
TIME_ZONE = 'EST'
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)
PAGE_LANGUAGES = (
    ('en-us', gettext_noop('US English')),
)

ALLOWED_HOSTS = (
    '*',
    #'www.compute.amazonaws.com',
    #'compute.amazonaws.com',
    #'localhost',
)

#==============================================================================
# Logging / Errors
#==============================================================================
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
# }

if IS_ON_SERVER:    

    # -- See: bit.ly/1gyIsW8
    # -- Don't set to True, causes an Error with Debug Toolbar in Production
    DEBUG_TOOLBAR_PATCH_SETTINGS = False

    #Sentry / RAVEN Set your DSN value
    RAVEN_CONFIG = {
        'dsn': 'https://00000000000000000000000000:00000000000000000000000000@app.getsentry.com/',
    }

#TEMP -- turn off debug panel
DEBUG_TOOLBAR_PATCH_SETTINGS = False

#==============================================================================
# Auth / security
#==============================================================================
SECRET_KEY = ')(SD*FSKLj3kjwned(*#$LKkk3j&SDH!~}{Da;ds}|34[f0sdJ'

DEFAULT_PASSWORD = 'disciplinereport2016'

AUTHENTICATION_BACKENDS += ()
AUTH_USER_MODEL = 'account.User'
USER_GROUP_MODEL = 'account.UserGroup'
ORGANIZATION_MODEL = 'account.Organization'

LOGIN_URL = '/admin/login/'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

if IS_ON_SERVER:    
    ALLOWED_HOSTS = ['disciplinereport.herokuapp.com', '.disciplinereport.com', 
        '.disciplinereport.com.', 'disciplinereport.s3.amazonaws.com', 's3.amazonaws.com',]


#==============================================================================
# Apps
#==============================================================================    

INSTALLED_APPS = (
    'reversion',
    'grappelli.dashboard',
    'grappelli',
    'localflavor',

    #'storages',
    #'haystack',
    'imagekit',
    'robots',
    'ckeditorfiles',
    'django_ace',#
    'ace_overlay',
    'django_inline_wrestler',
    'imagekit_cropper',
    'django_unsaved_changes', 
    'django_batch_uploader',  
    'simple_social_suture',

    'carbon.atoms',
    
    'share_me_share_me',

    'disciplinereport.apps.account',
    'disciplinereport.apps.media',   
    'disciplinereport.apps.core',
    'disciplinereport.apps.email',
    'disciplinereport.apps.form',
    'disciplinereport.apps.page',
    'disciplinereport.apps.data',
        

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    
    'django_extensions',
    'debug_toolbar',
    'raven.contrib.django.raven_compat',

)



#==============================================================================
# URL Settings
#==============================================================================
ROOT_URLCONF = 'disciplinereport.urls'
APPEND_SLASH = True

LEGACY_URL_CHOICES = ('page', 'form')
LEGACY_URL_MODEL = 'core.LegacyURL'
LEGACY_URL_ARCHIVE_DOMAIN = 'http://disciplinereport.com'
LEGACY_URL_IGNORE_LIST = []

#==============================================================================
# Media settings
#==============================================================================
AWS_ACCESS_KEY_ID       = env.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY   = env.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env.get("AWS_STORAGE_BUCKET_NAME", 'disciplinereport-dev')
AWS_STORAGE_BUCKET_NAME_MEDIA = env.get("AWS_STORAGE_BUCKET_NAME_MEDIA", 'disciplinereport-dev')


AWS_STATIC_FOLDER = 'static'
AWS_MEDIA_FOLDER = 'media'
AWS_S3_CUSTOM_DOMAIN    = '%s.s3.amazonaws.com'%(AWS_STORAGE_BUCKET_NAME)
AWS_S3_CUSTOM_DOMAIN_MEDIA    = '%s.s3.amazonaws.com'%(AWS_STORAGE_BUCKET_NAME_MEDIA)

AWS_STORAGE_BUCKET_NAME_MEDIA_SECURE = env.get("AWS_STORAGE_BUCKET_NAME_MEDIA_SECURE", 'disciplinereport-secure-dev')
AWS_S3_CUSTOM_DOMAIN_MEDIA_SECURE    = '%s.s3.amazonaws.com'%(AWS_STORAGE_BUCKET_NAME_MEDIA_SECURE)


AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
    'Expires': 'Thu, 15 Apr 2010 20:00:00 GMT',
    'Cache-Control': 'max-age=86400',
}

CKEDITOR_UPLOAD_PATH = "uploads/"

MEDIA_ROOT = ''
if env.get("MEDIA_URL", None):
    MEDIA_URL = "//%s/%s/" % (env.get("MEDIA_URL"), AWS_MEDIA_FOLDER)
    SECURE_MEDIA_URL = "//%s/%s/" % (env.get("SECURE_MEDIA_URL"), AWS_MEDIA_FOLDER)
else:
    MEDIA_URL = "//%s.s3.amazonaws.com/%s/" % (AWS_STORAGE_BUCKET_NAME_MEDIA, AWS_MEDIA_FOLDER)
    SECURE_MEDIA_URL = "//%s.s3.amazonaws.com/%s/" % (AWS_STORAGE_BUCKET_NAME_MEDIA_SECURE, AWS_MEDIA_FOLDER)

AWS_IS_GZIPPED = True
GZIP_CONTENT_TYPES = (
    'text/css',
    'application/javascript',
    'application/x-javascript',
    'text/javascript',
)

DEFAULT_FILE_STORAGE = 'disciplinereport.s3utils.MediaS3BotoStorage'
MEDIA_MODEL = 'media.Media'
SECURE_MEDIA_MODEL = 'media.SecureMedia'
MEDIA_STORAGE = 'disciplinereport.s3utils.MediaS3BotoStorage'
SECURE_MEDIA_STORAGE = 'disciplinereport.s3utils.SecureMediaS3BotoStorage'
SECURE_IMAGE_STORAGE = 'disciplinereport.s3utils.SecureImageS3BotoStorage'
IMAGE_MODEL_DELETE_FILE_ON_DELETE = True
DOCUMENT_MODEL_DELETE_FILE_ON_DELETE = True

IMAGE_THUMBNAIL_WIDTH = 200
IMAGE_THUMBNAIL_HEIGHT = None
IMAGE_THUMBNAIL_QUALITY = 95
IMAGE_MODEL = 'media.Image'
IMAGE_STORAGE = 'disciplinereport.s3utils.MediaS3BotoStorage'
SECURE_DOCUMENT_MODEL = 'media.SecureMedia'
#==============================================================================
# STATIC settings
#==============================================================================

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, AWS_MEDIA_FOLDER),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

if IS_ON_SERVER:
    
    VAR_ROOT = '/srv/http/carbon_media'

    STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
        
    STATICFILES_STORAGE = 'disciplinereport.s3utils.StaticS3BotoStorage'
    STATIC_URL = "//%s.s3.amazonaws.com/static/" % AWS_STORAGE_BUCKET_NAME

    AWS_S3_SECURE_URLS = True
    

else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')  



#==============================================================================
# Templates
#==============================================================================
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
    'carbon.compounds.core.loader.DBTemplateLoader',
)


TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)


TEMPLATE_CONTEXT_PROCESSORS += (
    
    'django.template.context_processors.csrf',
    'django.template.context_processors.request',

    'carbon.utils.context_processors.donottrack',
    'carbon.utils.context_processors.site',
    'carbon.utils.context_processors.custom_settings',
)


#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES = (
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'carbon.utils.middleware.Django403Middleware',
    'carbon.utils.middleware.DoNotTrackMiddleware',
    'carbon.utils.middleware.SiteMiddlewear',
    'carbon.utils.middleware.CustomSettingsMiddlewear',
    'carbon.utils.middleware.ImpersonateMiddleware', 
    'carbon.utils.middleware.AdminLoggedInCookieMiddlewear',
    'carbon.utils.middleware.SiteVersionMiddleware',
    'carbon.compounds.core.middleware.LegacyURLMiddleware',

)

if IS_ON_HEROKU or IS_ON_SERVER==False:
    MIDDLEWARE_CLASSES += (
        'django.middleware.gzip.GZipMiddleware',
    )


MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware', 
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
)
   

# 'django.contrib.auth.middleware.AuthenticationMiddleware',
# 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',

#==============================================================================
# Database
#==============================================================================
# if IS_ON_HEROKU:
#     DATABASES = herokuify.get_db_config()   # Database config
# else:

DATABASES = {
    'default': {
        'ENGINE': env.get('DB_DRIVER'),
        'HOST': env.get('DB_HOST'),
        'NAME': env.get('DB_NAME'),
        'USER': env.get('DB_USER'),
        'PASSWORD': env.get('DB_PASSWORD'),
        'PORT': env.get('PORT')
    }
}



#==============================================================================
# Caches
#==============================================================================


CACHES = herokuify.get_cache_config()   # Memcache config for Memcache/MemCachier
CACHES['dbtemplates'] = CACHES['default']
DBTEMPLATES_CACHE_BACKEND = "dbtemplates"

CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 2 #only cache views for a few hours
CACHE_DURATION = 60 * 60 * 24 * 30  

IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = 'imagekit.cachefiles.strategies.Optimistic'

#==============================================================================
# Search
#==============================================================================

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'disciplinereport',
    },
}

if env.get("SEARCH_HOST"):
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'URL': env.get("SEARCH_HOST"),
            'INDEX_NAME': env.get("SEARCH_INDEX_NAME",),
            'TIMEOUT': 60
        },
    }

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


#==============================================================================
# Email Settings
#==============================================================================
HELP_EMAIL = "support@disciplinereport.com"
HELP_PHONE = '123-456-7890'
DEFAULT_FROM_EMAIL = env.get("EMAIL_SENDER", "support@disciplinereport.com")
DEFAULT_FROM_EMAIL_NAME = SITE_TITLE

EMAIL_BACKEND = env.get("EMAIL_BACKEND", 'django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = env.get("EMAIL_HOST")
EMAIL_HOST_USER = env.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env.get("EMAIL_PORT", 587)
EMAIL_USE_TLS = env.get("EMAIL_TLS", True)

EMAIL = {
    'backend'   : EMAIL_BACKEND,
    'host'      : EMAIL_HOST,
    'port'      : EMAIL_PORT,
    'user'      : EMAIL_HOST_USER,
    'password'  : EMAIL_HOST_PASSWORD,
    'tls'       : EMAIL_USE_TLS
}

#==============================================================================
# DJANGO-CARBON SETTINGS
#==============================================================================
TEMPLATE_MODEL = 'core.Template'
PAGE_MODEL = 'page.Page'
MENU_MODEL = 'core.MenuItem'
MENU_MODEL_CHOICES = ('page',)



FORMS_DOMAIN = 'forms'
EMAIL_DOMAIN = 'email'


# Char to start a quoted choice with.
FORM_CHOICES_QUOTE = "`"
FORM_CHOICES_UNQUOTE = "`"

EMAIL_TEMPLATE_MODEL = 'email.EmailTemplate'
EMAIL_CATEGORY_MODEL = 'email.EmailCategory'
EMAIL_RECEIPT_MODEL = 'email.EmailReceipt'
EMAIL_SUBSCRIPTION_MODEL = 'email.UserSubscriptionSettings'
EMAIL_CATEGORY_SUBSCRIPTION_MODEL = 'email.EmailCategorySubscriptionSettings'
EMAIL_NOTIFICATION_CATEGORY_MODEL = 'email.EmailNotificationCategory'
DEFAULT_EMAIL_TEMPLATE_SLUG = 'base-email-template'

NEWS_LIST_DOMAIN = 'news'
NEWS_DETAIL_DOMAIN = 'news'
NEWS_LIST_VIEW = 'news_list'
NEWS_DETAIL_VIEW = 'news_detail'

NEWS_TAG_DOMAIN = 'news/tags'

SOLUTION_DETAIL_DOMAIN = 'solutions'
SOLUTION_LIST_DOMAIN = 'solutions'
SOLUTION_LIST_VIEW = 'solution_list'
SOLUTION_DETAIL_VIEW = 'solution_detail'

MARKET_DETAIL_DOMAIN = 'markets'
MARKET_LIST_DOMAIN = 'markets'
MARKET_LIST_VIEW = 'market_list'
MARKET_DETAIL_VIEW = 'market_detail'

CASE_STUDY_DETAIL_DOMAIN = 'case-studies'
CASE_STUDY_LIST_DOMAIN = 'case-studies'
CASE_STUDY_LIST_VIEW = 'case_study_list'
CASE_STUDY_DETAIL_VIEW = 'case_study_detail'


CLIENT_ACCESS_LIST_SLUG = 'client-support'
CLIENT_ACCESS_DETAIL_SLUG = 'client-support-detail'
PRODUCT_DOCUMENTATION_DETAIL_SLUG = 'product-documentation'

RENTAL_DETAIL_DOMAIN = 'rental-products'
RENTAL_LIST_DOMAIN = 'rental-products'
RENTAL_LIST_VIEW = 'rental_list'
RENTAL_DETAIL_VIEW = 'rental_detail'

#==============================================================================
# Third Pary Settings and API Keys
#==============================================================================
TWITTER_APP_KEY = env.get('TWITTER_APP_KEY')
TWITTER_APP_KEY_SECRET = env.get('TWITTER_APP_KEY_SECRET')
TWITTER_ACCESS_TOKEN = env.get('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = env.get('TWITTER_ACCESS_TOKEN_SECRET')
INSTAGRAM_CLIENT_ID = env.get('INSTAGRAM_CLIENT_ID')
INSTAGRAM_SECRET_CLIENT_ID = env.get('INSTAGRAM_SECRET_CLIENT_ID')
INSTAGRAM_ACCESS_TOKEN = env.get('INSTAGRAM_ACCESS_TOKEN')

FACEBOOK_CLIENT_ID = ''
FACEBOOK_SECRET_CLIENT_ID = ''

MAX_TWITTER_COUNT = 100
MAX_QUERY_COUNT = 200

ZOHO_AUTH_KEY   = env.get("ZOHO_AUTH_KEY")
HEROKU_API_KEY = env.get("HEROKU_API_KEY")



#=============================================================================
# ADMIN Settings
#=============================================================================
UNSAVED_CHANGES_UNSAVED_CHANGES_ALERT = True
UNSAVED_CHANGES_SUMBITTED_ALERT = True
UNSAVED_CHANGES_SUBMITTED_OVERLAY = True
UNSAVED_CHANGES_UNSAVED_CHANGES_VISUALS = True
UNSAVED_CHANGES_PERSISTANT_STORAGE = False #not quite production ready

FULL_CKEDITOR = {
    'skin': 'moono',
    'toolbar_Basic': [
        ['Source', '-', 'Bold', 'Italic']
    ],
    'toolbar_Full': [
        ['Format', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript','Superscript','SpellChecker', 'SpecialChar', 'Undo', 'Redo'],
        ['NumberedList', 'BulletedList', 'Blockquote'],
        ['Link', 'Unlink', 'Anchor'],
        ['Image', 'Iframe','Flash', 'Table', 'HorizontalRule', 'PageBreak'],
        ['PasteText', 'PasteFromWord', 'RemoveFormat'],
        ['showblocks', 'Source', 'Maximize'],
    ],
    'extraPlugins': 'magicline',
    'magicline_everywhere': 'true',
    'magicline_color': '#4fb2d3',
    'toolbar': 'Full',
    'height': 600,
    'width': 1000,
    'filebrowserWindowWidth': 940,
    'filebrowserWindowHeight': 725,
    'filebrowserImageBrowseUrl': '/admin/media/imagepicker/',
    'forcePasteAsPlainText' : 'true'
}
SMALL_CKEDITOR = {
    'skin': 'moono',
    'toolbar_Basic': [
        ['Source', '-', 'Bold', 'Italic']
    ],
    'toolbar_Full': [
        ['Format', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript','Superscript','SpellChecker', 'SpecialChar', 'Undo', 'Redo'],
        ['NumberedList', 'BulletedList', 'Blockquote'],
        ['Link', 'Unlink', 'Anchor'],
        ['PasteText', 'PasteFromWord', 'RemoveFormat'],
        ['showblocks', 'Source', 'Maximize'],
    ],
    'extraPlugins': 'magicline',
    'magicline_everywhere': 'true',
    'magicline_color': '#4fb2d3',
    'toolbar': 'Full',
    'height': 200,
    'width': 1000,
    'filebrowserWindowWidth': 940,
    'filebrowserWindowHeight': 725,
    'filebrowserImageBrowseUrl': '/admin/media/imagepicker/',
    'forcePasteAsPlainText' : 'true'
}
FULL_CKEDITOR_SHORT = copy.deepcopy(FULL_CKEDITOR)
FULL_CKEDITOR_SHORT['height'] = 250;


#Styles
CKEDITOR_CONFIGS = {
    'default': copy.deepcopy(FULL_CKEDITOR),
    'page_content_ckeditor': copy.deepcopy(FULL_CKEDITOR),
    'page_synopsis_ckeditor': copy.deepcopy(SMALL_CKEDITOR),
    'pagecontentblock_content_ckeditor': copy.deepcopy(FULL_CKEDITOR_SHORT),
    'pagecontentblock_synopsis_ckeditor': copy.deepcopy(SMALL_CKEDITOR),
    'user_about_ckeditor': copy.deepcopy(SMALL_CKEDITOR),
    'usergroup_content_ckeditor': copy.deepcopy(SMALL_CKEDITOR),
    'usergroup_synopsis_ckeditor': copy.deepcopy(SMALL_CKEDITOR),
}



CUSTOM_SETTINGS = ('STATIC_URL', 'IS_ON_SERVER','DEBUG','USE_SEARCH_INDEX',
    'SITE_ID','SITE_TITLE','HELP_EMAIL', 'HELP_PHONE'
    'SECURE_MEDIA_URL', 'MEDIA_URL', 'USE_SSL','SITE_DESCRIPTION',
    'CACHE_DURATION')


#Import file with all the hardcoded paths and values
from disciplinereport.settings.content_settings import *
