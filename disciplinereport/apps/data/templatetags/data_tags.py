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
def get_city_regions():
    return CityRegion.objects.all()

@register.assignment_tag()
def get_state_regions():
    return StateRegion.objects.all()

@register.assignment_tag()
def get_school_types():
    return SchoolType.objects.all()

@register.assignment_tag()
def get_value_difference(object, attribute):
    return object.get_value_difference(attribute)


