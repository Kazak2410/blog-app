from django.urls import path
from .views import HomePageView, AboutPageView, TopicListView, TopicDetailView


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('about/', AboutPageView.as_view(), name='about_page'),
    path('topic/', TopicListView.as_view(), name='topic_page'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
]