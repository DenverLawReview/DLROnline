from django.views.generic import ListView, DetailView
from .models import SymposiumPage

class SymposiaList(ListView):
    model = SymposiumPage
    context_object_name = 'symposia'

class SymposiumDetail(DetailView):
    model = SymposiumPage
    context_object_name = 'symposium'
