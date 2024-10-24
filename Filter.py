from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()


people_named_john = Person.objects.filter(first_name='John')

# multiple conditions 
people_named_john = Person.objects.filter(first_name='John', last_name='Doe')

