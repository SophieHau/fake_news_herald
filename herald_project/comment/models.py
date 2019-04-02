from django.db import models
from article.models import Article


class User(models.Model):
	name = models.CharField(max_length=50) 

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
	text = models.TextField()
	pub_date = models.DateTimeField('date published')

	class Meta:
		ordering = ['-pub_date']

