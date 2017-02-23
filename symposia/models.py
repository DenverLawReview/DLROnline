from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class SymposiumPage(models.Model):
    headline = models.CharField(max_length=100)
    slug = models.SlugField()
    volume = models.PositiveSmallIntegerField()
    blurb = models.TextField(null=True, blank=True)
    content = RichTextUploadingField()
    visible = models.BooleanField()
    reg_link = models.URLField('Registration Link', null=True, blank=True)

    class Meta:
        ordering = ['-volume']

    def __str__(self):
        return self.headline