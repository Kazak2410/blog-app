from django.views.generic import ListView, DetailView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs[::-1]


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
