from django import forms
from django.conf import settings

from ckeditorfiles.widgets import CKEditorWidget, CKEditorInlineWidget
from .models import CaseStudy, CustomerAccess

class CaseStudyAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config=settings.CKEDITOR_CONFIGS['page_content_ckeditor']), required=False)
    synopsis = forms.CharField(widget=CKEditorWidget(config=settings.CKEDITOR_CONFIGS['page_synopsis_ckeditor']), required=False)
    client_testimonial = forms.CharField(widget=CKEditorWidget(config=settings.CKEDITOR_CONFIGS['page_synopsis_ckeditor']), required=False)
    
    class Meta:
        model = CaseStudy
        fields = '__all__'

class CustomerAccessAdminForm(forms.ModelForm):
    client_notes = forms.CharField(widget=CKEditorWidget(config=settings.CKEDITOR_CONFIGS['page_synopsis_ckeditor']), required=False)
    
    class Meta:
        model = CustomerAccess
        fields = '__all__'


class ClientAccessForm(forms.Form):
    access_key = forms.CharField(label='Access Key', max_length=100)


