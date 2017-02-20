from django.conf.urls import include, url
from django.contrib import admin
from articles.views import ArticleList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ArticleList.as_view(), name='home'),
    url(r'^articles/', include('articles.urls')),
    url(r'^symposia/', include('symposia.urls')),
    url(r'^announcements/', include('announcements.urls')),
]
