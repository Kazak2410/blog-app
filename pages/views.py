from django.views.generic import TemplateView, ListView
from articles.models import Article, Category


class HomePageView(ListView):
    model = Article
    template_name = 'home_page.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs[::-1]


class AboutPageView(TemplateView):
    template_name = 'about_page.html'


class TopicListView(ListView):
    model = Category
    template_name = 'topic_page.html'


class TopicDetailView(ListView):
    model = Article
    template_name = 'topic_detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(category_id=self.request.resolver_match.kwargs.get('pk'))[::-1]
