from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.utils.decorators import method_decorator

from carbon.compounds.form.views import CreateFormEntryMixin
from carbon.compounds.page.views import PageDetail as BasePageDetail
from carbon.compounds.page.views import PageTagView as BasePageTagView
from carbon.compounds.page.views import PageBlockView as BasePageBlockView

from carbon.compounds.form.views import signal_form_error, signal_form_entry_created

from .models import Page
from disciplinereport.apps.form.forms import FormEntryForm
from disciplinereport.apps.form.models import Form, FormEntry
# from disciplinereport.utils.crm import handle_form_entry


class PageDetail(BasePageBlockView, CreateFormEntryMixin, BasePageDetail):

    model = Page
    form_class = FormEntryForm

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(PageDetail, self).dispatch(*args, **kwargs)

    def get_form_schema(self):
        if not self.object:
            self.object = self.get_object()
        if self.object:
            return self.object.form
        return None


    def get_success_url(self):
        return self.object.get_absolute_url()


@receiver(signal_form_error, sender=Form)
def on_form_error(sender, **kwargs):
    form = kwargs['form_schema']
    #pass...

@receiver(signal_form_entry_created, sender=FormEntry)
def on_form_created(sender, **kwargs):
    pass
    # form_entry = kwargs['form_entry']
    # if settings.IS_ON_SERVER == True:
    #     handle_form_entry(form_entry)   
    # else:
    #     print '--- handle form entry local ---'     