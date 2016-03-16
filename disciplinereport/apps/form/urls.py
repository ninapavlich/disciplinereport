from django.conf.urls.static import static
from django.conf.urls import patterns, url, include

from .views import *

urlpatterns = patterns('',
    url( (r'^%s/(?P<path>.*)/(?P<pk>\d+)/$'%settings.FORMS_DOMAIN), UpdateFormEntryView.as_view(), name='form_update_view'),   
)

