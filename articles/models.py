from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='D:\\projects\\blog\\static\\images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        reverse('article_detail', args=[str(self.id)])


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
