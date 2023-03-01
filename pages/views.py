from django.views.generic import TemplateView, ListView
from articles.models import Article


class HomePageView(ListView):
    model = Article
    template_name = 'home_page.html'


class AboutPageView(TemplateView):
    template_name = 'about_page.html'