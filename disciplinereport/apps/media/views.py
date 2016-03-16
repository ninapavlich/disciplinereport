from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.db.models.loading import get_model
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import TemplateView


from .models import *

from carbon.compounds.media.views import ImagePickerView as BaseImagePickerView
from carbon.compounds.media.views import ImageBatchView as BaseImageBatchView
from carbon.compounds.media.views import SecureImageBatchView as BaseSecureImageBatchView
from carbon.compounds.media.views import DocumentBatchView as BaseDocumentBatchView
from carbon.compounds.media.views import SecureDocumentBatchView as BaseSecureDocumentBatchView

class ImagePickerView(BaseImagePickerView):
    pass


class ImageBatchView(BaseImageBatchView):      
    model = Image


class DocumentBatchView(BaseDocumentBatchView):      
    model = Media
