from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.utils.html import escape, format_html, format_html_join, smart_urlquote
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from imagekit_cropper.widgets import ImageCropWidget    

from .models import *





class ImageAdminForm(forms.ModelForm):
    square_crop = forms.CharField(widget=ImageCropWidget(properties=Image.square_crop_properties, help_text=Image.help['square_crop']), required=False)


    wide_crop = forms.CharField(widget=ImageCropWidget(properties=Image.wide_crop_properties, help_text=Image.help['wide_crop']), required=False)
    
    class Meta:
        model = Image
        fields = '__all__'