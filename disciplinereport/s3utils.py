from django.conf import settings
from django.utils.deconstruct import deconstructible
from storages.backends.s3boto import S3BotoStorage



@deconstructible
class _StaticS3BotoStorage(S3BotoStorage):
    pass

StaticS3BotoStorage = lambda: _StaticS3BotoStorage(
        location=settings.AWS_STATIC_FOLDER,
        bucket=settings.AWS_STORAGE_BUCKET_NAME,
        custom_domain=settings.AWS_S3_CUSTOM_DOMAIN
    )

@deconstructible
class _MediaS3BotoStorage(S3BotoStorage):
    pass

MediaS3BotoStorage = lambda: _MediaS3BotoStorage(
        location=settings.AWS_MEDIA_FOLDER,
        bucket=settings.AWS_STORAGE_BUCKET_NAME_MEDIA,
        custom_domain=settings.AWS_S3_CUSTOM_DOMAIN_MEDIA
    )

@deconstructible
class _SecureMediaS3BotoStorage(S3BotoStorage):
    pass

SecureMediaS3BotoStorage = lambda: _SecureMediaS3BotoStorage(
        location=settings.AWS_MEDIA_FOLDER,
        bucket=settings.AWS_STORAGE_BUCKET_NAME_MEDIA_SECURE,
        custom_domain=settings.AWS_S3_CUSTOM_DOMAIN_MEDIA_SECURE
    )


@deconstructible
class _SecureImageS3BotoStorage(S3BotoStorage):
    pass

SecureImageS3BotoStorage = lambda: _SecureMediaS3BotoStorage(
        location=settings.AWS_MEDIA_FOLDER,
        bucket=settings.AWS_STORAGE_BUCKET_NAME_MEDIA_SECURE,
        custom_domain=settings.AWS_S3_CUSTOM_DOMAIN_MEDIA_SECURE
    )
