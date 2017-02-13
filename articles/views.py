from django.views.generic import ListView, DetailView
from .models import Article, Category, PrintIssue, OnlineIssue

class ArticleList(ListView):
    model = Article

class ArticleDetail(DetailView):
    model = Article

class CategoryList(ListView):
    model = Category

class CategoryDetail(DetailView):
    model = Category

class PrintIssueList(ListView):
    model = PrintIssue

class PrintIssueDetail(DetailView):
    model = PrintIssue

class OnlineIssueList(ListView):
    model = OnlineIssue

class OnlineIssueDetail(DetailView):
    model = OnlineIssue
