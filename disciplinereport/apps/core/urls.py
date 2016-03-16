from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	
	url(r'^admin/utils/import/links/$', admin_import_links, name='admin_import_links'),
)