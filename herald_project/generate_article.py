from faker import Faker
from article.models import Article, Author
from django.utils import timezone
import random

fake = Faker()

def generate_fake_title():
	return fake.sentence()

def generate_fake_subtitle():
	return fake.sentence() + fake.sentence() + fake.sentence()

def generate_fake_text():
	return fake.text(1000)

def generate_random_author():
	authors = Author.objects.all()
	author = random.choice(authors)
	return author

def generate_fake_article(number):
	for i in range(0, number):
		a = Article(
			article_title=generate_fake_title(), 
			article_subtitle=generate_fake_subtitle(), 
			article_text=generate_fake_text(), 
			author=generate_random_author(),
			pub_date=timezone.now())
		a.save()