from django.contrib import admin


from carbon.compounds.form.admin import FormAdmin as BaseFormAdmin
from carbon.compounds.form.admin import FormFieldInline as BaseFormFieldInline
from carbon.compounds.form.admin import FieldEntryAdmin as BaseFieldEntryAdmin
from carbon.compounds.form.admin import FormEntryAdmin as BaseFormEntryAdmin
from carbon.compounds.form.admin import FieldEntryInline as BaseFieldEntryInline
from carbon.compounds.form.admin import FormEntryStatusAdmin as BaseFormEntryStatusAdmin
from carbon.compounds.form.admin import FormEntryTagAdmin as BaseFormEntryTagAdmin

from carbon.compounds.form.forms import FormFieldInlineAdminForm
from carbon.compounds.form.forms import FormAdminForm

from django_unsaved_changes.admin import UnsavedChangesAdmin

from .models import *



class FormEntryStatusAdmin(BaseFormEntryStatusAdmin, UnsavedChangesAdmin):
    pass

class FormEntryTagAdmin(BaseFormEntryTagAdmin, UnsavedChangesAdmin):
    pass

class FormFieldInline(BaseFormFieldInline):
    model = FormField
    form = FormFieldInlineAdminForm
    
class FormAdmin(BaseFormAdmin, UnsavedChangesAdmin):
    form = FormAdminForm
    inlines = [FormFieldInline]    
    pass
 
class FieldEntryInline(BaseFieldEntryInline):
	model = FieldEntry

class FormEntryAdmin(BaseFormEntryAdmin, UnsavedChangesAdmin):
	inlines = [FieldEntryInline]

	def content_preview(self, obj):
		entries = obj.get_fields_with_entries()
		first_few = entries[:2]
		output = ''
		for item in first_few:
			output += "<strong>%s</strong> %s<br />"%(item['title'], item['value'])
		return output
	content_preview.allow_tags = True

	list_display = BaseFormEntryAdmin.list_display + ('content_preview',)

admin.site.register(Form, FormAdmin)
admin.site.register(FormEntry, FormEntryAdmin)
admin.site.register(FormEntryStatus, FormEntryStatusAdmin)
admin.site.register(FormEntryTag, FormEntryTagAdmin)