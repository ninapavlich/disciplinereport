from django.db import models
from django.conf import settings

from carbon.compounds.core.models import Template as BaseTemplate
from carbon.compounds.core.models import CSSPackage as BaseCSSPackage
from carbon.compounds.core.models import JSPackage as BaseJSPackage
from carbon.compounds.core.models import CSSResource as BaseCSSResource
from carbon.compounds.core.models import JSResource as BaseJSResource
from carbon.compounds.core.models import AdminAppGroup as BaseAdminAppGroup
from carbon.compounds.core.models import AdminAppLink as BaseAdminAppLink
from carbon.compounds.core.models import AdminSidebar as BaseAdminSidebar
from carbon.compounds.core.models import AdminLink as BaseAdminLink

from carbon.compounds.core.models import MenuItem as BaseMenuItem
from carbon.compounds.core.models import LegacyURL as BaseLegacyURL
from carbon.compounds.core.models import LegacyURLReferer as BaseLegacyURLReferer


class Template(BaseTemplate):
    pass   

class CSSResource(BaseCSSResource):
    pass

class JSResource(BaseJSResource):
    pass

class CSSPackage(BaseCSSPackage):
	item_class = CSSResource

class JSPackage(BaseJSPackage):
	item_class = JSResource



class MenuItem(BaseMenuItem):
    pass
    
class AdminAppLink( BaseAdminAppLink ):
	pass

class AdminAppGroup( BaseAdminAppGroup ):
    item_class = AdminAppLink

class AdminLink( BaseAdminLink ):
	pass

class AdminSidebar( BaseAdminSidebar ):
    item_class = AdminLink

class LegacyURL(BaseLegacyURL):
    pass

class LegacyURLReferer(BaseLegacyURLReferer):
    legacy_url = models.ForeignKey('LegacyURL')

