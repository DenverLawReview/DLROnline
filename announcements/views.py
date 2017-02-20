from django.views.generic import ListView, DetailView
from .models import Announcement


class AnnouncementList(ListView):
    model = Announcement
    context_object_name = 'announcements'

class AnnouncementDetail(DetailView):
    model = Announcement
    context_object_name = 'announcement'
