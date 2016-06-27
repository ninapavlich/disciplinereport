from django.contrib import admin

from carbon.compounds.account.admin import UserAdmin as BaseUserAdmin
from carbon.compounds.account.admin import OrganizationAdmin as BaseOrganizationAdmin
from carbon.compounds.account.admin import UserGroupMemberInGroupAdmin as BaseUserGroupMemberInGroupAdmin
from carbon.compounds.account.admin import UserGroupMemberInUserAdmin as BaseUserGroupMemberInUserAdmin
from carbon.compounds.account.admin import UserGroupAdmin as BaseUserGroupAdmin
from carbon.compounds.account.admin import SocialContactLinkInline as BaseSocialContactLinkInline

from .models import *

from django_unsaved_changes.admin import UnsavedChangesAdmin


class UserGroupMemberInGroupAdmin(BaseUserGroupMemberInGroupAdmin):
    model = UserGroupMember    

class UserGroupMemberInUserAdmin(BaseUserGroupMemberInUserAdmin):
    model = UserGroupMember    

class SocialContactLinkInline(BaseSocialContactLinkInline):
    model = SocialContactLink    

class OrganizationSocialContactLinkInline(BaseSocialContactLinkInline):
    model = OrganizationSocialContactLink      
    fk_name = 'organization'  

class UserAdmin(BaseUserAdmin, UnsavedChangesAdmin):
    inlines = [UserGroupMemberInUserAdmin, SocialContactLinkInline]

    fieldsets = (
        ('User', { 
            'fields': (
                ("first_name","last_name"),
                'project_role',
                ('email',),
                'password',
                'about',
                ('preview','image')
            ),
            'classes': ( 'grp-collapse grp-open', )
        }),
        ('CMS Permissions', {
            'fields': (
                ('is_active', 'is_staff',),
                
                'is_superuser',
                ('groups')
            ),
            'classes': ( 'grp-collapse grp-closed', )
        }),
    )

class UserGroupAdmin(BaseUserGroupAdmin, UnsavedChangesAdmin):
    inlines = [UserGroupMemberInGroupAdmin]

class OrganizationAdmin(BaseOrganizationAdmin, UnsavedChangesAdmin):
    core_fields = (
        ('title','slug'),
        ('synopsis')
    )
    address_fields = (
        ('street_1','street_2'),
        ('city', 'state'),
        ('zipcode'),
        ('latitude', 'longitude'),
    )
    

    meta_fields = BaseOrganizationAdmin.meta_fields
    fieldsets = (
        ("Main Body", {
            'fields': core_fields,
            'classes': ( 'grp-collapse grp-open', )
        }),
        ("Address", {
            'fields': address_fields,
            'classes': ( 'grp-collapse grp-open', )
        }),
        ("Meta", {
            'fields': meta_fields,
            'classes': ( 'grp-collapse grp-closed', )
        })
    )
    search_fields = ('title','admin_note', 'synopsis', 'content')
    inlines = [OrganizationSocialContactLinkInline]
    

admin.site.register(Organization, OrganizationAdmin)    
admin.site.register(User, UserAdmin)
admin.site.register(UserGroup, UserGroupAdmin)