from django.db import models
from imagekit.models import ProcessedImageField

class Post(models.Model):
    title = models.TextField(blank = True,null = True)
    image = ProcessedImageField (
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True,
    )

class Post2(models.Model):
    title = models.TextField(blank = True,null = True)
    image = ProcessedImageField (
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True,
    )