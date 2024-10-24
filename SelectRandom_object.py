from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)



import random
random_person = Person.objects.order_by('?').first()

# or,

# Count the number of objects
count = Person.objects.count()

# Generate a random index
random_index = random.randint(0, count - 1)

# Retrieve the object at the random index
random_person = Person.objects.all()[random_index]
