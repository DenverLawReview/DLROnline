from django.db import models
from django.utils import timezone


class PublishedAnnouncementManager(models.Manager):
    def get_queryset(self):
        return super(PublishedAnnouncementManager, self).get_queryset().filter(published=True, pub_date__lte=timezone.now())


class Announcement(models.Model):
    headline = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=100)
    pub_date = models.DateTimeField('date published')
    published = models.BooleanField()

    objects = models.Manager()
    published_announcements = PublishedAnnouncementManager()

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.headline
