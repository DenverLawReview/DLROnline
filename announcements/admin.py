from django.contrib import admin
from django.db import models
from .models import Announcement
from ckeditor.widgets import CKEditorWidget

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date', 'published')
    list_editable = ['published']
    list_filter = ('published',)
    search_fields = ['headline']
    date_hierarchy = 'pub_date'
    prepopulated_fields = {"slug": ("headline",)}
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }


admin.site.register(Announcement, AnnouncementAdmin)
