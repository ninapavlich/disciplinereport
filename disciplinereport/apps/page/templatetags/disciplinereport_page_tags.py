from django.template import Library
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.safestring import mark_safe
from django.core.exceptions import ImproperlyConfigured
try:
    from django.apps import apps
    get_model = apps.get_model
except:
    from django.db.models.loading import get_model
    
from ..models import *

register = Library()



@register.assignment_tag()
def get_content_block_by_slug(slug=None):
   
    try:
        item = GlobalContentBlock.objects.get(slug=slug)
    except:
        item = None

    return item