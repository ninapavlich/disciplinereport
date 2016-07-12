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

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *


class SchoolDistrictResource(resources.ModelResource):

    class Meta:
        model = SchoolDistrict


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

class SchoolDistrictDatumAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


class SchoolDistrictDatumInline(admin.TabularInline):
    model = SchoolDistrictDatum
    extra = 0
    fields = ['school_year', 'population', 'soc', 'frl', 'ell', 'sped', 'iss', 
        'oss', 'expulsions', 'rtl', 'one_offense', 'school_arrests',
        'racial_disparity_impact', 'district_inequality_contribution',
        'student_turnover', 'poor_attendance', 'proficient_math', 
        'proficient_reading', 'proficient_writing' ]



class SchoolDistrictAdmin(ImportExportModelAdmin, BaseEntityAdmin):
    core_fields = (
        ('edit_parent','parent'),
        ('title','slug'),
        ('publication_status'),
        ('email','website',),
        'phone_number',
        ('street_1','street_2'),
        ('city','state',),
        'zipcode',
        ('latitude','longitude')
    )


    path_fields = BaseEntityAdmin.path_fields
    seo_fields = BaseEntityAdmin.seo_fields
    meta_fields = BaseEntityAdmin.meta_fields

    fieldsets = (
        ("Main Content", {
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

    inlines = [SchoolDistrictDatumInline]

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

class SchoolYearAdmin(admin.ModelAdmin):
    pass



admin.site.register(State, StateAdmin)
admin.site.register(SchoolDistrict, SchoolDistrictAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(CityRegion, BaseTagAdmin)
admin.site.register(SchoolYear, SchoolYearAdmin)
admin.site.register(SchoolDistrictDatum, SchoolDistrictDatumAdmin)
