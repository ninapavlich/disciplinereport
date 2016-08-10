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
    return CityRegion.objects.all().order_by('title')

@register.assignment_tag()
def get_state_regions():
    return StateRegion.objects.all().order_by('title')

@register.assignment_tag()
def get_school_types():
    return SchoolType.objects.all().order_by('title')

@register.assignment_tag()
def get_school_districts():
    return SchoolDistrict.objects.all().order_by('title')

@register.assignment_tag()
def get_schools():
    return School.objects.all().order_by('title')

@register.assignment_tag()
def get_value_difference(object, attribute):
    return object.get_value_difference(attribute)

@register.assignment_tag()
def get_value_formatted(data, attribute_name):
    return data.format_field(attribute_name, getattr(data, attribute_name))


@register.assignment_tag()
def get_tooltips():
    return Tooltip.objects.all()

@register.assignment_tag()
def get_tooltip(slug):
    try:
        return Tooltip.objects.filter(slug=slug)[0]
    except:
        return None

@register.assignment_tag()
def get_state_data(school_district_datum):
    try:
        return StateDatum.objects.filter(school_year=school_district_datum.school_year,state=school_district_datum.school_district.state_obj)[0]
    except:
        return None



@register.assignment_tag(takes_context=True)
def is_checked(context, column_name, attribute):
    request = context['request']
    checkbox_value = request.GET.getlist(column_name, None)
    # print checkbox_value
    if not checkbox_value:
        return True
    is_checked = attribute in checkbox_value
    return is_checked