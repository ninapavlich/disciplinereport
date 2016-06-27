from django.contrib import admin
from django.core.urlresolvers import reverse

from reversion.admin import VersionAdmin

from carbon.atoms.admin.content import HierarchicalContentAdmin, BaseContentAdmin, BaseVersionableAdmin
from carbon.atoms.admin.content import BaseSlideInlineAdmin
from carbon.compounds.page.admin import PageAdmin as BasePageAdmin
from carbon.compounds.page.forms import PageAdminForm
from carbon.compounds.page.admin import PageTagAdmin as BasePageTagAdmin
from carbon.compounds.page.admin import PageContentBlockInline as BasePageContentBlockInline
from carbon.compounds.page.admin import GlobalContentBlockAdmin as BaseGlobalContentBlockAdmin

from django_unsaved_changes.admin import UnsavedChangesAdmin

from django_inline_wrestler.admin import TabularInlineOrderable

from .models import *

class BaseTagAdmin(VersionAdmin):
    pass



class BaseEntityAdmin(VersionAdmin, HierarchicalContentAdmin):
    # form = PageAdminForm

    autocomplete_lookup_fields = HierarchicalContentAdmin.autocomplete_lookup_fields
    
    m2m_fields_list = list(autocomplete_lookup_fields['m2m'])
    # m2m_fields_list.insert(0, 'tags')
    autocomplete_lookup_fields['m2m'] = tuple(m2m_fields_list)

    raw_id_fields = HierarchicalContentAdmin.raw_id_fields
    raw_id_fields_list = list(raw_id_fields)
    # raw_id_fields_list.insert(0, 'tags')
    raw_id_fields = tuple(raw_id_fields_list)

    core_fields = (
        ('edit_parent','parent'),
        ('title','slug'),
        ('publication_status')
    )
    
    path_fields = BaseContentAdmin.path_fields
    publication_fields = BaseContentAdmin.publication_fields
    seo_fields = (
        'page_meta_description',
        'page_meta_keywords',
        ('in_sitemap'),
        ('sitemap_changefreq','sitemap_priority'),
        ('noindex','nofollow')
    )
    social_fields = BaseContentAdmin.social_fields
    meta_fields = BaseVersionableAdmin.meta_fields

    fieldsets = (
        ("Main Body", {
            'fields': core_fields,
            'classes': ( 'grp-collapse grp-open', )
        }),
        
        ("Path", {
            'fields': path_fields,
            'classes': ( 'grp-collapse grp-closed', )
        }),
        ("Search Engine Optimization", {
            'fields': seo_fields,
            'classes': ( 'grp-collapse grp-closed', )
        }),
        ("Meta", {
            'fields': meta_fields,
            'classes': ( 'grp-collapse grp-closed', )
        })
    )


class StateAdmin(BaseEntityAdmin):
    core_fields = (
        ('edit_parent','parent'),
        ('title','slug'),
        ('publication_status'),
    )
    
    path_fields = BaseEntityAdmin.path_fields
    seo_fields = BaseEntityAdmin.seo_fields
    meta_fields = BaseEntityAdmin.meta_fields

    fieldsets = (
        ("Main Body", {
            'fields': core_fields,
            'classes': ( 'grp-collapse grp-open', )
        }),
        
        ("Path", {
            'fields': path_fields,
            'classes': ( 'grp-collapse grp-closed', )
        }),
        ("Search Engine Optimization", {
            'fields': seo_fields,
            'classes': ( 'grp-collapse grp-closed', )
        }),
        ("Meta", {
            'fields': meta_fields,
            'classes': ( 'grp-collapse grp-closed', )
        })
    )

class SchoolDistrictAdmin(BaseEntityAdmin):
    core_fields = (
        ('edit_parent','parent'),
        ('title','slug'),
        ('publication_status'),
    )
    
    path_fields = BaseEntityAdmin.path_fields
    seo_fields = BaseEntityAdmin.seo_fields
    meta_fields = BaseEntityAdmin.meta_fields

    fieldsets = (
        ("Main Body", {
            'fields': core_fields,
            'classes': ( 'grp-collapse grp-open', )
        }),
        
        ("Path", {
            'fields': path_fields,
            'classes': ( 'grp-collapse grp-closed', )
        }),
        ("Search Engine Optimization", {
            'fields': seo_fields,
            'classes': ( 'grp-collapse grp-closed', )
        }),
        ("Meta", {
            'fields': meta_fields,
            'classes': ( 'grp-collapse grp-closed', )
        })
    )

class SchoolAdmin(BaseEntityAdmin):
    core_fields = (
        ('edit_parent','parent'),
        ('title','slug'),
        ('publication_status'),
        'school_district',
        'city_region',
        ('is_charter','is_pathways')
    )
    
    path_fields = BaseEntityAdmin.path_fields
    seo_fields = BaseEntityAdmin.seo_fields
    meta_fields = BaseEntityAdmin.meta_fields

    fieldsets = (
        ("Main Body", {
            'fields': core_fields,
            'classes': ( 'grp-collapse grp-open', )
        }),
        
        ("Path", {
            'fields': path_fields,
            'classes': ( 'grp-collapse grp-closed', )
        }),
        ("Search Engine Optimization", {
            'fields': seo_fields,
            'classes': ( 'grp-collapse grp-closed', )
        }),
        ("Meta", {
            'fields': meta_fields,
            'classes': ( 'grp-collapse grp-closed', )
        })
    )


admin.site.register(State, StateAdmin)
admin.site.register(SchoolDistrict, SchoolDistrictAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(CityRegion, BaseTagAdmin)
