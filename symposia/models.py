from django.db import models


class SymposiumPage(models.Model):
    headline = models.CharField(max_length=100)
    slug = models.SlugField()
    event_date = models.DateField()
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
        limit_choices_to={'parent__isnull': True}, blank=True, null=True)
    visible = models.BooleanField()
