from django.db import models
from tinymce.models import HTMLField


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    image = models.ImageField(upload_to='blog/images', default='blog/images/default.svg')
    date = models.DateField()

    def __str__(self):
        return self.title
