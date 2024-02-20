from .models import Employee
from faker import Faker

fake = Faker()


def seed_db(n):
    for i in range(0, n):
        Employee.objects.create(name=fake.name(), age=fake.random_int(min=18, max=65))
