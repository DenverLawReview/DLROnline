from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager


class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super(PublishedArticleManager, self).get_queryset().filter(published=True, pub_date__lte=timezone.now())


class Article(models.Model):
    headline = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=100)
    pub_date = models.DateTimeField('date published')
    volume = models.PositiveSmallIntegerField()
    published = models.BooleanField()
    # Relationships
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    tags = TaggableManager()
    online_issue = models.ForeignKey('OnlineIssue', blank=True, null=True, on_delete=models.SET_NULL)
    print_issue = models.ForeignKey('PrintIssue', blank=True, null=True, on_delete=models.SET_NULL)

    objects = models.Manager()
    published_articles = PublishedArticleManager()

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.headline


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['title']

    def __str__(self):
        return self.title

    def published_articles(self):
        return Article.published_articles.filter(category=self)

class OnlineIssue(models.Model):
    title = models.CharField(max_length=100)
    introduction = models.TextField()
    slug = models.SlugField(max_length=100)
    visible = models.BooleanField()

    class Meta:
        verbose_name = "online issue"
        verbose_name_plural = "online issues"

    def __str__(self):
        return self.title

    def published_articles(self):
        return Article.published_articles.filter(online_issue=self)

class PrintIssue(models.Model):
    volume = models.PositiveSmallIntegerField()
    issue = models.PositiveSmallIntegerField()
    visible = models.BooleanField()

    class Meta:
        verbose_name = "print issue"
        verbose_name_plural = "print issues"
        ordering = ['-volume', '-issue']
        unique_together = ("volume", "issue")

    def __str__(self):
        return "Volume {}, Issue {}".format(self.volume, self.issue)

    def published_articles(self):
        return Article.published_articles.filter(print_issue=self)

