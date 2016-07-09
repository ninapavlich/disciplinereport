from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Q
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


class DistrictDetailView(BasePageDetail):
    
    model = SchoolDistrict
    catch_404s = False

    def get_template_names(self):
        if self.object and self.object.template:
            return [self.object.template.slug]
        return ['school-district-detail']