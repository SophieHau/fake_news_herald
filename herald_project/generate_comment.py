from faker import Faker
from comment.models import User, Comment
from article.models import Article
from django.utils import timezone
import random

fake = Faker()

def generate_fake_text():
	return fake.text(300)

def generate_random_user():
	users = User.objects.all()
	user = random.choice(users)
	return user

def generate_random_article():
	articles = Article.objects.all()
	article = random.choice(articles)
	return article

def generate_fake_comment(number):
	for i in range(0, number):
		c = Comment(
			user=generate_random_user(), 
			article=generate_random_article(), 
			text=generate_fake_text(), 
			pub_date=timezone.now()
			)
		c.save()