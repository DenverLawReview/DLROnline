from django.conf.urls import url
from .views import *

app_name = "articles"
urlpatterns = [
    # Articles
    url(r'^articles/$', ArticleList.as_view(), name='article-list'),
    url(r'^articles/(?P<pk>\d+)/(?P<slug>[-_\w]+)$',
        ArticleDetail.as_view(), name='article-detail'),
    # Categories
    url(r'^articles/categories/(?P<pk>\d+)/(?P<slug>[-_\w]+)$',
        CategoryDetail.as_view(), name='category-detail'),
    # Print Issues
    url(r'^articles/print-issues$', PrintIssueList.as_view(), name='print-issue-list'),
    url(r'articles/print-issues/(?P<pk>\d+)$', PrintIssueDetail.as_view(), name='print-issue-detail'),
    # Online Special Issues
    url(r'^articles/online-issues/$', OnlineIssueList.as_view(), name='online-issue-list'),
    url(r'^articles/online-issues/(?P<pk>\d+)/(?P<slug>[-_\w]+)$',
        OnlineIssueDetail.as_view(), name='online-issue-detail'),
]
