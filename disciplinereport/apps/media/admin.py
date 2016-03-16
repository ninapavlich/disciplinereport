from django.contrib import admin

from carbon.atoms.admin.media import FolderTagAdmin as BaseFolderTagAdmin
from carbon.compounds.media.admin import ImageAdmin as BaseImageAdmin
from carbon.compounds.media.admin import MediaAdmin as BaseMediaAdmin
from carbon.compounds.media.admin import SecureMediaAdmin as BaseSecureMediaAdmin
from carbon.compounds.media.admin import SecureImageAdmin as BaseSecureImageAdmin
from carbon.compounds.media.admin import MediaTagAdmin as BaseMediaTagAdmin
from carbon.compounds.media.admin import MediaFolderAdmin as BaseMediaFolderAdmin


from .models import *
from .forms import *

from django_unsaved_changes.admin import UnsavedChangesAdmin




class ImageAdmin(BaseFolderTagAdmin, BaseImageAdmin, UnsavedChangesAdmin):

    folder_model = ImageFolder
    tag_model = MediaTag
    batch_url_name = "admin_image_batch_view"

    form = ImageAdminForm

    core_fields = (
        'title',
        ('image'),

        ('square_crop', 'wide_crop'),
        ('dimensions'),
        ('image_variants_links'),
        
        
        ('clean_filename_on_upload','allow_overwrite'),
        ('alt','use_png'),
        'credit',
        'caption',
        'folder',
        'tags'
    )
    
    meta_fields = (
        ('version'),
        ('created_date', 'created_by'),
        ('modified_date', 'modified_by'),
        'file_modified_date',
        'admin_note'
    )

    fieldsets = (
        ("Image", {
            'fields': core_fields,
        }),
        ("Meta", {
            'fields': meta_fields,
            'classes': ( 'grp-collapse grp-closed', )
        })
    )

    readonly_fields = (
        "version", "created_date", "created_by", "modified_date", "modified_by",
        "preview", "image_variants_links", "image_width", "image_height",
        "display_size", "size", "dimensions", "file_modified_date"
    )

    autocomplete_lookup_fields = {
        'fk': ('folder',),
        'm2m': ('tags',)
    }
    raw_id_fields = ( 'tags','folder')

class SecureImageAdmin(BaseSecureImageAdmin, UnsavedChangesAdmin):

    

    core_fields = (
        'title',
        ('image','preview'),
        ('clean_filename_on_upload','allow_overwrite'),
        ('alt','use_png'),
        ('dimensions', 'image_variants'),
        'credit',
        'caption'
    )
    
    meta_fields = (
        ('version'),
        ('created_date', 'created_by'),
        ('modified_date', 'modified_by'),
        'file_modified_date',
        'admin_note'
    )

    fieldsets = (
        ("Image", {
            'fields': core_fields,
        }),
        ("Meta", {
            'fields': meta_fields,
            'classes': ( 'grp-collapse grp-closed', )
        })
    )




class MediaAdmin(BaseMediaAdmin, BaseFolderTagAdmin, UnsavedChangesAdmin):
    folder_model = MediaFolder
    tag_model = MediaTag

class SecureMediaAdmin(BaseSecureMediaAdmin):
    pass

class MediaTagAdmin(BaseMediaTagAdmin, UnsavedChangesAdmin):
    pass 


class MediaFolderAdmin(BaseMediaFolderAdmin, UnsavedChangesAdmin):
    pass 

class ImageFolderAdmin(BaseMediaFolderAdmin, UnsavedChangesAdmin):
    pass 


admin.site.register(Image, ImageAdmin)
admin.site.register(SecureImage, SecureImageAdmin)
admin.site.register(Media, MediaAdmin)    
admin.site.register(SecureMedia, SecureMediaAdmin)  
admin.site.register(MediaTag, MediaTagAdmin)        
admin.site.register(MediaFolder, MediaFolderAdmin)        
admin.site.register(ImageFolder, ImageFolderAdmin)        

