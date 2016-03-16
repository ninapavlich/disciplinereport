from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from carbon.compounds.form.models import Form as BaseForm
from carbon.compounds.form.models import FormField as BaseFormField
from carbon.compounds.form.models import FormEntry as BaseFormEntry
from carbon.compounds.form.models import FieldEntry as BaseFieldEntry
from carbon.compounds.form.models import FormEntryStatus as BaseFormEntryStatus
from carbon.compounds.form.models import FormEntryTag as BaseFormEntryTag


class FormEntryStatus(BaseFormEntryStatus):
    pass

class FormEntryTag(BaseFormEntryTag):
    pass


class FormField(BaseFormField):
	pass

class Form(BaseForm):
	field_model = FormField

class FieldEntry(BaseFieldEntry):
	pass
	
class FormEntry(BaseFormEntry):
	field_entry_model = FieldEntry



