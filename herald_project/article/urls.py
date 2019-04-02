from django.urls import path
from . import views

urlpatterns = [
	path('', views.show_articles, name='articles'),
	path('article/<int:article_id>', views.show_article, name='article'),
]