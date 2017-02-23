from django.conf.urls import include, url
from django.contrib import admin
from articles.views import ArticleList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ArticleList.as_view(template_name="home.html"), name='home'),
    url(r'^articles/', include('articles.urls')),
    url(r'^symposia/', include('symposia.urls')),
    url(r'^announcements/', include('announcements.urls')),
]
# Need this for the file uploader plugin.
urlpatterns += [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
