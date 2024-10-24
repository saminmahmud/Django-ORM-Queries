from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


# 1)
# Create a new Person object
new_person = Person(first_name='John', last_name='Doe')

# Save it to the database
new_person.save()


# 2)
new_person = Person.objects.create(first_name='Jane', last_name='Doe')


# 3)
# create multiple objects in one shot
Person.objects.bulk_create([
    Person(first_name='Alice', last_name='Smith'),
    Person(first_name='Bob', last_name='Jones'),
    Person(first_name='Charlie', last_name='Brown'),
])


# Creating and saving an object: Use new_person.save().
# Using create(): Saves an object in one step.
# Creating multiple objects: Use bulk_create() for efficiency.