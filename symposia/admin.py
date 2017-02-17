from django.contrib import admin
from .models import SymposiumPage

class SymposiumPageAdmin(admin.ModelAdmin):
    list_display = ('headline', 'event_date', 'parent', 'visible')
    list_editable = ['visible',]
    list_filter = ('visible',)
    search_fields = ['headline']
    date_hierarchy = 'event_date'
    # exclude = ('online_issue', 'print_issue')
    prepopulated_fields = {"slug": ("headline",)}

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/articles/tinymce_setup.js',
        ]

admin.site.register(SymposiumPage, SymposiumPageAdmin)
