from faker import Faker
from article.models import Author

fake = Faker()

def generate_fake_name():
	return fake.name()

def generate_fake_author(number):
	for i in range(0, number):
		a = Author(name=generate_fake_name())
		a.save()

