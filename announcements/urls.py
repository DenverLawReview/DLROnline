from django.conf.urls import url
from .views import *

app_name = "announcements"
urlpatterns = [
    # Articles
    url(r'^$', AnnouncementList.as_view(), name='announcement-list'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-_\w]+)$',
        AnnouncementDetail.as_view(), name='announcement-detail'),
]