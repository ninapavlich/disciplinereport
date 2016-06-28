from django.dispatch import receiver

from carbon.compounds.form.views import CreateFormEntryView as BaseCreateFormEntryView
from carbon.compounds.form.views import UpdateFormEntryView as BaseUpdateFormEntryView
from carbon.compounds.form.views import FormSubmittedView as BaseFormSubmittedView
from carbon.compounds.form.views import signal_form_entry_updated

from .models import *
from .forms import *

class CreateFormEntryView(BaseCreateFormEntryView):
    model = Form
    form_class = FormEntryForm

class UpdateFormEntryView(BaseUpdateFormEntryView):
    model = Form
    form_class = FormEntryForm
    form_entry_class = FormEntry


class FormSubmittedView(BaseFormSubmittedView):
    model = Form


@receiver(signal_form_entry_updated, sender=FormEntry)
def on_form_updated(sender, **kwargs):
    print "Form Updated: %s"%(kwargs)