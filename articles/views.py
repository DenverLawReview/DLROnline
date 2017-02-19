from django.views.generic import ListView, DetailView
from .models import Article, Category, PrintIssue, OnlineIssue

class ArticleList(ListView):
    context_object_name = 'articles'
    queryset = Article.published_articles.all()

class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Article.objects.all()
        else:
            return Article.published_articles.all()

class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'

class PrintIssueList(ListView):
    context_object_name = 'print_issues'
    queryset = PrintIssue.objects.filter(visible=True)

class PrintIssueDetail(DetailView):
    model = PrintIssue
    context_object_name = 'print_issue'

    def get_queryset(self):
        if self.request.user.is_staff:
            return PrintIssue.objects.all()
        else:
            return PrintIssue.objects.filter(visible=True)

class OnlineIssueList(ListView):
    context_object_name = 'online_issues'
    queryset = OnlineIssue.objects.filter(visible=True)

class OnlineIssueDetail(DetailView):
    model = OnlineIssue
    context_object_name = 'online_issue'

    def get_queryset(self):
        if self.request.user.is_staff:
            return OnlineIssue.objects.all()
        else:
            return OnlineIssue.objects.filter(visible=True)
