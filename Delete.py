from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

person_to_delete = Person.objects.get(id=1)  # Get the object by its ID
person_to_delete.delete()


# Delete a specific person
Person.objects.filter(first_name='John', last_name='Doe').delete()


Person.objects.all().delete() # Delete all


