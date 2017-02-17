from django.contrib import admin
from .models import Article, Category, OnlineIssue, PrintIssue

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'author', 'category', 'pub_date', 'published')
    list_editable = ['category', 'published']
    list_filter = ('published',)
    search_fields = ['headline']
    date_hierarchy = 'pub_date'
    # exclude = ('online_issue', 'print_issue')
    prepopulated_fields = {"slug": ("headline",)}

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/articles/tinymce_setup.js',
        ]

admin.site.register(Article, ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)

class OnlineIssueAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/articles/tinymce_setup.js',
        ]


admin.site.register(OnlineIssue, OnlineIssueAdmin)

class PrintIssueAdmin(admin.ModelAdmin):
    pass

admin.site.register(PrintIssue, PrintIssueAdmin)
