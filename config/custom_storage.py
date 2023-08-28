# from django.conf import settings
# from storages.backends.s3boto3 import S3Boto3Storage
# 
# 
# class MediaStorage(S3Boto3Storage):
#     location = 'media'
# 
#     def __init__(self, *args, **kwargs):
#         kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
#         super(MediaStorage, self).__init__(*args, **kwargs)
# 
#     def _clean_name(self, name):
#         return name
# 
#     def _normalize_name(self, name):
#         if name.startswith('/'):
#             return self.location + name
#         else:
#             return self.location + '/' + name
