from django.db import models


class Author(models.Model):
	name = models.CharField(max_length=50)

class Article(models.Model):
	article_title = models.CharField(max_length=200)
	article_subtitle = models.CharField(max_length=300)
	article_text = models.TextField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published')


