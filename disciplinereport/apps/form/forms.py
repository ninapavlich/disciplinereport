from django import forms

from carbon.compounds.form.forms import FormEntryForm as BaseFormEntryForm

from .models import *

class FormEntryForm(BaseFormEntryForm):
    field_model = FieldEntry
    
    class Meta:
        model = FormEntry
        fields = ['form_schema']