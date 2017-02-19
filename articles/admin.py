from django import forms
from django.db import models
from django.contrib import admin
from .models import Article, Category, OnlineIssue, PrintIssue
from ckeditor.widgets import CKEditorWidget

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'author', 'category', 'pub_date', 'published')
    list_editable = ['category', 'published']
    list_filter = ('published',)
    search_fields = ['headline']
    date_hierarchy = 'pub_date'
    exclude = ('online_issue', 'print_issue')
    prepopulated_fields = {"slug": ("headline",)}
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class OnlineIssueSelectForm(forms.ModelForm):
    articles = forms.ModelMultipleChoiceField(queryset=Article.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple("Articles", is_stacked=False))

    def __init__(self, *args, **kwargs):
        super(OnlineIssueSelectForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['articles'].initial = self.instance.article_set.all()

    def save(self, *args, **kwargs):
        instance = super(OnlineIssueSelectForm, self).save(commit=False)
        self.fields['articles'].initial.update(online_issue=None)
        self.cleaned_data['articles'].update(online_issue=instance)
        return instance


class OnlineIssueAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = OnlineIssueSelectForm


class PrintIssueSelectForm(forms.ModelForm):
    articles = forms.ModelMultipleChoiceField(queryset=Article.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple("Articles", is_stacked=False))

    def __init__(self, *args, **kwargs):
        super(PrintIssueSelectForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['articles'].initial = self.instance.article_set.all()

    def save(self, *args, **kwargs):
        instance = super(PrintIssueSelectForm, self).save(commit=False)
        self.fields['articles'].initial.update(print_issue=None)
        self.cleaned_data['articles'].update(print_issue=instance)
        return instance

class PrintIssueAdmin(admin.ModelAdmin):
    form = PrintIssueSelectForm


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OnlineIssue, OnlineIssueAdmin)
admin.site.register(PrintIssue, PrintIssueAdmin)
