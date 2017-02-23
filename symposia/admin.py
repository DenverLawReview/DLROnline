from django.contrib import admin
from .models import SymposiumPage
from django.db import models
from ckeditor.widgets import CKEditorWidget

class SymposiumPageAdmin(admin.ModelAdmin):
    list_display = ('headline', 'volume', 'visible')
    list_editable = ['visible',]
    list_filter = ('visible',)
    search_fields = ['headline']
    prepopulated_fields = {"slug": ("headline",)}
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.register(SymposiumPage, SymposiumPageAdmin)
