from faker import Faker
from comment.models import User

fake = Faker()

def generate_fake_name():
	return fake.name()

def generate_fake_user(number):
	for i in range(0, number):
		u = User(name=generate_fake_name())
		u.save()

