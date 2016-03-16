from carbon.compounds.email.views import EmailOnlineView as BaseEmailOnlineView
from carbon.compounds.email.views import EmailSettingsView as BaseEmailSettingsView
from carbon.compounds.email.views import EmailRecordView as BaseEmailRecordView
from carbon.compounds.email.views import EmailRenderedView as BaseEmailRenderedView

from .models import *
from .forms import *

class EmailOnlineView(BaseEmailOnlineView):
	template_slug = 'email_online'
	model = EmailReceipt

class EmailRenderedView(BaseEmailRenderedView):
	model = EmailReceipt

class EmailSettingsView(BaseEmailSettingsView):
	template_slug = 'email_settings'	
	model = UserSubscriptionSettings
	
class EmailRecordView(BaseEmailRecordView):

	model = EmailReceipt