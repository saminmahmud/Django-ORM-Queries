# Django তে select_related একটি QuerySet পদ্ধতি, যা সম্পর্কিত অবজেক্টগুলোকে একসাথে, একক SQL query এর মাধ্যমে আনার জন্য ব্যবহৃত হয়। এটি বিশেষ করে ForeignKey বা OneToOne সম্পর্কের ক্ষেত্রে কার্যকর।


# ধরি, আপনার কাছে নিচের মডেলগুলো আছে:
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


# আপনি যদি বই এবং তাদের লেখকদের তথ্য একসাথে নিয়ে আসতে চান, তবে select_related ব্যবহার করতে পারেন:
books = Book.objects.select_related('author').all()

for book in books:
    print(f"{book.title} by {book.author.name}")


queryset = Book.objects.select_related('author', 'publisher')



