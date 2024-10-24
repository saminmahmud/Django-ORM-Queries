from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

distinct_names = Person.objects.values('first_name', 'last_name').distinct()

for name in distinct_names:
    print(f"First Name: {name['first_name']}, Last Name: {name['last_name']}")

