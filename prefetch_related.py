# Django-তে prefetch_related একটি QuerySet পদ্ধতি, যা সম্পর্কিত অবজেক্টগুলোকে আলাদা Query দিয়ে নিয়ে আসে, বিশেষ করে যখন আপনি ManyToMany বা reverse ForeignKey সম্পর্কের সাথে কাজ করছেন। এটি কার্যকরী যখন আপনি একটি সম্পর্কিত মডেল থেকে অনেকগুলো অবজেক্ট একসাথে নিয়ে আসতে চান।


# ধরি, আপনার কাছে নিম্নলিখিত মডেলগুলো আছে:
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)


# এখন, যদি আপনি বই এবং তাদের লেখকদের তথ্য একসাথে আনতে চান, তবে prefetch_related ব্যবহার করবেন:
books = Book.objects.prefetch_related('authors').all()


