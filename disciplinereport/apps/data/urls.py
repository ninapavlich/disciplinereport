from django.conf import settings
from django.conf.urls import patterns, url, include

from .views import *

urlpatterns = patterns('',

    url( (r'^%s/$'%settings.DISTRICT_LIST_DOMAIN), DistrictListView.as_view(), {'path': "/%s"%(settings.DISTRICT_LIST_DOMAIN)}, name='district_list' ), 
    url( r'^%s/(?P<path>[-_\/\w]*)$'%(settings.DISTRICT_DETAIL_DOMAIN), DistrictDetailView.as_view(), name="district_detail" ),
    url( r'^%s/(?P<path>.*)$'%(settings.DISTRICT_DETAIL_DOMAIN), DistrictDetailView.as_view(), name="district_detail" ),
)
