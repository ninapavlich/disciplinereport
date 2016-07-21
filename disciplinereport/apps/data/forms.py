from django import forms
from django.conf import settings

from ckeditorfiles.widgets import CKEditorWidget, CKEditorInlineWidget
from .models import Tooltip

class TooltipAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config=settings.CKEDITOR_CONFIGS['page_synopsis_ckeditor']), required=False)
    
    class Meta:
        model = Tooltip
        fields = '__all__'



