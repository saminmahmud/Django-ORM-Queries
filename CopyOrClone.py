class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def clone(self):
        # Create a new instance without the primary key
        cloned_person = Person(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
        )
        return cloned_person


original_person = Person.objects.get(id=1)
cloned_person = original_person.clone()
cloned_person.save()


# Retrieve the original object using get().