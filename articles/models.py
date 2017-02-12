from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    headline = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=100)
    pub_date = models.DateTimeField('date published')
    volume = models.PositiveSmallIntegerField()
    published = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, limit_choices_to={'is_superuser': True})
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.headline


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title
