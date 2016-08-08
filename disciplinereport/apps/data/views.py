import csv
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import ProcessFormView, FormMixin
from django.http import Http404


from django.views.generic import DetailView
from carbon.compounds.page.views import PageDetail as BasePageDetail
from carbon.compounds.page.views import PageTagView as BasePageTagView
from carbon.compounds.page.views import SiblingPageDetail as BaseSiblingPageDetail
from carbon.atoms.views.abstract import *
from carbon.atoms.views.content import *

from disciplinereport.apps.page.models import Page
from .models import *


# HasChildrenView, 
class BaseListView(NonAdminCachableView, PublishableView, AddressibleView, HasChildrenView, DetailView):
    children = []
    #list_model = Name

    def get_children(self):
        children = self.list_model.objects.all()
        return [child for child in children if child.is_published()]


class DistrictListView(BaseListView):
    model = Page
    list_model = SchoolDistrict

    def get_filter_title(self):
        region_slugs = self.request.GET.getlist('regions[]', None)
        
        
        initial_label =  "Showing 1 school district" if len(self.children) == 1 else "Showing %s school districts"%(len(self.children)) 
        
        if region_slugs:
            regions = StateRegion.objects.filter(slug__in=region_slugs)
            region_label = " in the "+(", ".join([region.title for region in regions]))
        else:
            region_label = ' in all regions'


        label = initial_label+region_label
        return label
        

    def get_context_data(self, **kwargs):
        context = super(DistrictListView, self).get_context_data(**kwargs)
        context['filter_title'] = self.get_filter_title()
        return context


    def get_children(self):
        children = self.list_model.objects.all().select_related('state_obj').select_related('state_region').select_related('county')

        regions = self.request.GET.getlist('regions[]', None)
        if regions:
            children = [child for child in children if child.state_region.slug in regions]

        return [child for child in children if child.is_published()]

    


class DistrictDetailView(BasePageDetail):
    
    model = SchoolDistrict
    catch_404s = False

    def get_template_names(self):
        if self.object and self.object.template:
            return [self.object.template.slug]
        return ['school-district-detail']

def district_list_download_view(request):

    objects = SchoolDistrict.objects.all()
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="district-data.csv"'

    writer = format_data(response, objects)


    return response

def district_detail_download_view(request, path):

    object = SchoolDistrict.objects.get(slug=path)
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s.csv"'%(path)

    writer = format_data(response, [object])

    return response

def format_data(response, objects):

    writer = csv.writer(response)

    ctr = 0
    for object in objects:
        for row in object.data:
            
            row_values = row.column_values
            if ctr == 0:
                header_columns = []
                for column in row_values:
                    header_columns.append(column['title'])

                writer.writerow(header_columns)
            
            ctr = ctr+1

            data_columns = []
            for column in row_values:
                data_columns.append(column['value'])
            writer.writerow(data_columns)

    return response    