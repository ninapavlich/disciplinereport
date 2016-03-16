from django.contrib import admin

from carbon.compounds.core.admin import TemplateAdmin as BaseTemplateAdmin
from carbon.compounds.core.admin import CSSPackageAdmin as BaseCSSPackageAdmin
from carbon.compounds.core.admin import JSPackageAdmin as BaseJSPackageAdmin

from carbon.compounds.core.admin import CSSResourceAdmin as BaseCSSResourceAdmin
from carbon.compounds.core.admin import JSResourceAdmin as BaseJSResourceAdmin
from carbon.compounds.core.admin import CSSResourceInline as BaseCSSResourceInline
from carbon.compounds.core.admin import JSResourceInline as BaseJSResourceInline

from carbon.compounds.core.admin import MenuItemInline as BaseMenuItemInline
from carbon.compounds.core.admin import MenuItemAdmin as BaseMenuItemAdmin
from carbon.compounds.core.admin import AdminAppLinkInline as BaseAdminAppLinkInline
from carbon.compounds.core.admin import AdminLinkInline as BaseAdminLinkInline
from carbon.compounds.core.admin import AdminAppGroupAdmin as BaseAdminAppGroupAdmin
from carbon.compounds.core.admin import AdminSidebarAdmin as BaseAdminSidebarAdmin

from carbon.compounds.core.admin import LegacyURLRefererInline as BaseLegacyURLRefererInline
from carbon.compounds.core.admin import LegacyURLAdmin as BaseLegacyURLAdmin

from django_unsaved_changes.admin import UnsavedChangesAdmin

from .models import *

class TemplateAdmin(BaseTemplateAdmin, UnsavedChangesAdmin):
    pass


class CSSResourceAdmin(BaseCSSResourceAdmin, UnsavedChangesAdmin):
    pass

class JSResourceAdmin(BaseJSResourceAdmin, UnsavedChangesAdmin):
    pass

class CSSResourceInline(BaseCSSResourceInline):
    model = CSSResource

class JSResourceInline(BaseJSResourceInline):
    model = JSResource

class CSSPackageAdmin(BaseCSSPackageAdmin, UnsavedChangesAdmin):
    inlines = [CSSResourceInline]

class JSPackageAdmin(BaseJSPackageAdmin, UnsavedChangesAdmin):
    inlines =[JSResourceInline]    


class MenuItemInline(BaseMenuItemInline):
    model = MenuItem
    
class MenuItemAdmin(BaseMenuItemAdmin, UnsavedChangesAdmin):
    inlines = [MenuItemInline]


class AdminAppLinkInline(BaseAdminAppLinkInline):
    model = AdminAppLink

class AdminLinkInline(BaseAdminLinkInline):

    model = AdminLink
  
class AdminAppGroupAdmin(BaseAdminAppGroupAdmin, UnsavedChangesAdmin):
    inlines = [AdminAppLinkInline]

class AdminSidebarAdmin(BaseAdminSidebarAdmin, UnsavedChangesAdmin):
    inlines = [AdminLinkInline]


class LegacyURLRefererInline(BaseLegacyURLRefererInline):
    model = LegacyURLReferer
    
class LegacyURLAdmin(BaseLegacyURLAdmin, UnsavedChangesAdmin):
    inlines = [LegacyURLRefererInline]    
    pass




admin.site.register(Template, TemplateAdmin)
admin.site.register(CSSPackage, CSSPackageAdmin)
admin.site.register(JSPackage, JSPackageAdmin)
admin.site.register(CSSResource, CSSResourceAdmin)
admin.site.register(JSResource, JSResourceAdmin)

admin.site.register(AdminAppGroup, AdminAppGroupAdmin)
admin.site.register(AdminSidebar, AdminSidebarAdmin)
admin.site.register(LegacyURL, LegacyURLAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
