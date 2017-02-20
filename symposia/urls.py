from django.conf.urls import url
from .views import *

app_name = "symposia"
urlpatterns = [
    # Articles
    url(r'^$', SymposiaList.as_view(), name='symposia-list'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-_\w]+)$',
        SymposiumDetail.as_view(), name='symposia-detail'),
]