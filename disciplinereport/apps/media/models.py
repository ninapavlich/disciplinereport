import copy

from django.db import models
from django.conf import settings

from imagekit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ImageSpecField

from imagekit_cropper.fields import ImageCropField, InstanceSpecField, InstanceFormatSpecField
from imagekit_cropper.processors import PositionCrop, PositionAndFormatCrop, FormatProcessor


from carbon.compounds.media.models import Image as BaseImage
from carbon.compounds.media.models import SecureImage as BaseSecureImage
from carbon.compounds.media.models import Media as BaseMedia
from carbon.compounds.media.models import SecureMedia as BaseSecureMedia
from carbon.compounds.media.models import MediaTag as BaseMediaTag
from carbon.compounds.media.models import MediaFolder as BaseMediaFolder
from carbon.compounds.media.models import MediaPositionCrop, MediaFormatProcessor, MediaPositionAndFormatCrop

   




class ImageVariantMixin(object):
    """
    DEPRECATED
    """
    pass


class Image(BaseImage):
    
    tags = models.ManyToManyField('media.MediaTag', blank=True, related_name='%(app_label)s_%(class)s_tags')
    folder = models.ForeignKey('media.ImageFolder', null=True, blank=True, related_name='%(app_label)s_%(class)s_folder')

    variants = ('thumbnail',
        'square_200', 'width_200_fill', 
        'square_400', 'width_400_fill','width_400_wide',
        'square_600', 'width_600_fill', 'width_600_wide',
        'width_800_fill', 
        'width_1000_fill','width_1000_wide',
        'width_1200_fill','width_1200_wide',)


    help = {
        'square_crop':'Square Crop',
        'wide_crop':'2:1 aspect ratio',

        'square_150_crop': '150px by 150px crop',
        'square_150': '150px by 150px',

        'square_200_crop': '200px by 200px crop',
        'square_200': '200px by 200px',
        'width_200_fill_crop':'200px, upscaled',
        'width_200_fill':'Can be upscaled',

        'square_400_crop': '400px by 400px crop',
        'square_400': '400px by 400px',
        'width_400_fill_crop':'400px, upscaled',
        'width_400_fill':'Can be upscaled',
        
        
        'square_600_crop':'600px by 600px crop',
        'square_600':'600px by 600px',
        'width_600_fill_crop':'600px, upscaled',
        'width_600_fill':'Can be upscaled',

        'width_800_crop':'800px wide, no upscale',
        'width_800':'800px, no upscale',
        'width_800_fill_crop':'800px, upscaled',
        'width_800_fill':'Can be upscaled',

        'width_1000_fill_crop':'1000px, upscaled',
        'width_1000_fill':'Can be upscaled',
        
        'width_1200_fill_crop': '1200px wide, no upscale',
        'width_1200_fill': 'No upscale',
        'width_1200_wide_crop':'1200px by 600px crop',
        'width_1200_wide':'1200x600'
        
    }

    # square_150 = ImageSpecField( source='image', format='PNG',
    #     processors=[ResizeToFill(150, 150)], options={'quality': 85})

    # square_150_crop_properties = {
    #     'source':'image',
    #     'crop_field':'square_150_crop', 
    #     'resize_method':'fill',
    #     'width':150,
    #     'height':150, 
    #     'upscale':False
    # }
    # square_150_crop = ImageCropField(null=True, blank=True, 
    #     properties=square_150_crop_properties, help_text=help['square_150_crop'])
    # square_150_processor = PositionCrop(square_150_crop_properties)
    # square_150 = InstanceSpecField(
    #     format='JPEG',
    #     source=square_150_crop_properties['source'], 
    #     options={'quality': 85}, 
    #     processors=[square_150_processor]
    # )


    square_crop_properties = {
        'source':'image',
        'crop_field':'square_crop', 
        'format_field':'get_format',
        'resize_method':'fill',
        'aspect_ratio':1,
        'min_width':600,
        'min_height':600,
        'upscale':True
    }
    

    wide_crop_properties = {
        'source':'image',
        'crop_field':'wide_crop', 
        'format_field':'get_format',
        'resize_method':'fill',
        'width':1200,
        'height':600, 
        'upscale':True
    }


    #------- 200px Wide -------
    square_200_crop_properties = copy.copy(square_crop_properties)
    square_200_crop_properties['width'] = 200
    square_200_crop_properties['height'] = 200
    
    square_200 = InstanceSpecField(
        format='PNG',
        source=square_200_crop_properties['source'], 
        options={'quality': 85}, 
        processors=[MediaPositionCrop(square_200_crop_properties)]
    )

    width_200_fill_crop_properties = {
        'source':'image',
        'format_field':'get_format',
        'resize_method':'fit',
        'width':200,
        'height':None, 
        'upscale':True
    }
    width_200_fill = InstanceFormatSpecField( 
        source=width_200_fill_crop_properties['source'], 
        format_field=width_200_fill_crop_properties['format_field'],
        options={'quality': 85}, 
        processors=[MediaFormatProcessor(width_200_fill_crop_properties)])


    #------- 400px Wide -------
    square_400_crop_properties = copy.copy(square_crop_properties)
    square_400_crop_properties['width'] = 400
    square_400_crop_properties['height'] = 400

    square_400 = InstanceFormatSpecField(
        source=square_400_crop_properties['source'], 
        format_field=square_400_crop_properties['format_field'],
        options={'quality': 85}, 
        processors=[MediaPositionAndFormatCrop(square_400_crop_properties)]
    )
    width_400_fill_crop_properties = {
        'source':'image',
        'format_field':'get_format',
        'resize_method':'fit',
        'width':400,
        'height':None, 
        'upscale':True
    }
    width_400_fill = InstanceFormatSpecField( 
        source=width_400_fill_crop_properties['source'], 
        format_field=width_400_fill_crop_properties['format_field'],
        options={'quality': 85}, 
        processors=[MediaFormatProcessor(width_400_fill_crop_properties)])

    width_400_wide_crop_properties = {
        'source':'image',
        'crop_field':'width_1200_wide_crop', 
        'format_field':'get_format',
        'resize_method':'fill',
        'width':400,
        'height':400, 
        'upscale':True
    }


    width_400_wide_crop_properties = copy.copy(wide_crop_properties)
    width_400_wide_crop_properties['width'] = 400
    width_400_wide_crop_properties['height'] = 200
    width_400_wide = InstanceFormatSpecField( 
        source=width_400_wide_crop_properties['source'], 
        format_field=width_400_wide_crop_properties['format_field'],
        options={'quality': 95}, 
        processors=[MediaPositionAndFormatCrop(width_400_wide_crop_properties)])

    #------- 600px Wide -------
    square_600_crop_properties = copy.copy(square_crop_properties)
    square_600_crop_properties['width'] = 600
    square_600_crop_properties['height'] = 600

    square_600 = InstanceFormatSpecField( 
        source=square_600_crop_properties['source'], 
        format_field=square_600_crop_properties['format_field'],
        options={'quality': 85}, 
        processors=[MediaPositionAndFormatCrop(square_600_crop_properties)])
    width_600_fill_crop_properties = {
        'source':'image',
        'format_field':'get_format',
        'resize_method':'fit',
        'width':600,
        'height':None, 
        'upscale':True
    }
    width_600_fill = InstanceFormatSpecField( 
        source=width_600_fill_crop_properties['source'], 
        format_field=width_600_fill_crop_properties['format_field'],
        options={'quality': 95}, 
        processors=[MediaFormatProcessor(width_600_fill_crop_properties)])

    width_600_wide_crop_properties = copy.copy(wide_crop_properties)
    width_600_wide_crop_properties['width'] = 600
    width_600_wide_crop_properties['height'] = 300
    width_600_wide = InstanceFormatSpecField( 
        source=width_600_wide_crop_properties['source'], 
        format_field=width_600_wide_crop_properties['format_field'],
        options={'quality': 95}, 
        processors=[MediaPositionAndFormatCrop(width_600_wide_crop_properties)])

    #------- 800px Wide ------- 
    width_800_fill_crop_properties = {
        'source':'image',
        'format_field':'get_format',
        'resize_method':'fit',
        'width':800,
        'height':None, 
        'upscale':True
    }
    width_800_fill = InstanceFormatSpecField( 
        source=width_800_fill_crop_properties['source'], 
        format_field=width_800_fill_crop_properties['format_field'],
        options={'quality': 95}, 
        processors=[MediaFormatProcessor(width_800_fill_crop_properties)])

    #------- 1000px Wide -------
    width_1000_fill_crop_properties = {
        'source':'image',
        'format_field':'get_format',
        'resize_method':'fit',
        'width':1000,
        'height':None, 
        'upscale':True
    }
    
    width_1000_fill = InstanceFormatSpecField( 
        source=width_1000_fill_crop_properties['source'], 
        format_field=width_1000_fill_crop_properties['format_field'],
        options={'quality': 95}, 
        processors=[MediaFormatProcessor(width_1000_fill_crop_properties)])

    width_1000_wide_crop_properties = copy.copy(wide_crop_properties)
    width_1000_wide_crop_properties['width'] = 1000
    width_1000_wide_crop_properties['height'] = 500
    width_1000_wide = InstanceFormatSpecField( 
        source=width_1000_wide_crop_properties['source'], 
        format_field=width_1000_wide_crop_properties['format_field'],
        options={'quality': 95}, 
        processors=[MediaPositionAndFormatCrop(width_1000_wide_crop_properties)])

    #------- 1200px Wide -------

    
    

    width_1200_wide_crop_properties = copy.copy(wide_crop_properties)
    width_1200_wide_crop_properties['width'] = 1200
    width_1200_wide_crop_properties['height'] = 600
    width_1200_wide = InstanceFormatSpecField( 
        source=width_1200_wide_crop_properties['source'], 
        format_field=width_1200_wide_crop_properties['format_field'],
        options={'quality': 95}, 
        processors=[MediaPositionAndFormatCrop(width_1200_wide_crop_properties)])


    width_1200_fill_crop_properties = {
        'source':'image',
        'format_field':'get_format',
        'resize_method':'fit',
        'width':1200,
        'height':None, 
        'upscale':True
    }
    
    width_1200_fill = InstanceFormatSpecField( 
        source=width_1200_fill_crop_properties['source'], 
        format_field=width_1200_fill_crop_properties['format_field'],
        options={'quality': 95}, 
        processors=[MediaFormatProcessor(width_1200_fill_crop_properties)])

    square_crop = ImageCropField(null=True, blank=True, 
        properties=square_crop_properties)
    
    wide_crop = ImageCropField(null=True, blank=True, 
        properties=wide_crop_properties, 
        help_text=help['wide_crop'])

    width_1000_fill_crop = ImageCropField(null=True, blank=True, 
        properties=width_1000_fill_crop_properties, 
        help_text=help['width_1000_fill_crop'])

    width_1200_fill_crop = ImageCropField(null=True, blank=True, 
        properties=width_1200_fill_crop_properties, 
        help_text=help['width_1200_fill_crop'])

class SecureImage(BaseSecureImage):
    
    variants = ('thumbnail',)
    


class Media(BaseMedia):
    
    tags = models.ManyToManyField('media.MediaTag', blank=True, related_name='%(app_label)s_%(class)s_tags')
    folder = models.ForeignKey('media.MediaFolder', null=True, blank=True, related_name='%(app_label)s_%(class)s_folder')


class SecureMedia(BaseSecureMedia):
    pass    
# class SecureMedia(BaseSecureMedia):
#     pass

class MediaTag(BaseMediaTag):
    publish_by_default = True
    item_classes = [Image, Media] #SecureMedia   

class ImageFolder(BaseMediaFolder):
    item_classes = [Image]
    category_property_name = 'folder'  

class MediaFolder(BaseMediaFolder):
    item_classes = [Media]
    category_property_name = 'folder'  

