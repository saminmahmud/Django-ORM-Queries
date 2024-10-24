from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()


# single field, ascending order
people = Person.objects.all().order_by('first_name')


# multiple fields
people = Person.objects.all().order_by('last_name', 'first_name')


# Descending order
people = Person.objects.all().order_by('-first_name')  # Descending order


# Combining Ascending and Descending
people = Person.objects.all().order_by('last_name', '-first_name')


from django.db.models import Count
# Example: Order by the number of related objects (if applicable)
people = Person.objects.annotate(num_related=Count('some_related_model')).order_by('-num_related')


# Use a minus sign (-) for descending order.

