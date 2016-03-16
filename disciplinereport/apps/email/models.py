from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from carbon.compounds.email.models import EmailTemplate as BaseEmailTemplate
from carbon.compounds.email.models import EmailCategory as BaseEmailCategory
from carbon.compounds.email.models import EmailReceipt as BaseEmailReceipt
from carbon.compounds.email.models import UserSubscriptionSettings as BaseUserSubscriptionSettings
from carbon.compounds.email.models import EmailCategorySubscriptionSettings as BaseEmailCategorySubscriptionSettings



class EmailTemplate(BaseEmailTemplate):
    pass

class EmailCategory(BaseEmailCategory):
    pass

class EmailReceipt(BaseEmailReceipt):
    pass


class UserSubscriptionSettings(BaseUserSubscriptionSettings):
	pass

class EmailCategorySubscriptionSettings(BaseEmailCategorySubscriptionSettings):
    pass
