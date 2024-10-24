# Django ORM-এ Subquery Expression ব্যবহার করে আপনি একটি কোয়েরির ভিতরে অন্য একটি কোয়েরি চালাতে পারেন। এটি একটি খুব শক্তিশালী ফিচার, যা আপনাকে জটিল ডেটাবেজ অপারেশন সম্পন্ন করতে সাহায্য করে।
# Subquery হল একটি কোয়েরি যা আরেকটি কোয়েরির মধ্যে ব্যবহৃত হয়। এটি মূলত একটি "কোয়েরির ভিতরে কোয়েরি"।


from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)


# ধরি, আমরা লেখকদের মধ্যে সেই লেখকদের খুঁজে বের করতে চাই, যাদের অন্তত একটি বইয়ের দাম ৫০-এর বেশি।
from django.db.models import OuterRef, Subquery

# প্রথম কোয়েরি: প্রথমে আমরা সেই বইগুলো খুঁজব যেগুলোর দাম ৫০-এর বেশি।
expensive_books = Book.objects.filter(price__gt=50, author=OuterRef('pk'))

# দ্বিতীয় কোয়েরি: এখন আমরা লেখকদের খুঁজব যারা এই বইগুলোর লেখক।
authors = Author.objects.filter(pk__in=Subquery(expensive_books.values('author')))

for author in authors:
    print(author.name)


# OuterRef: এটি মূল কোয়েরির লেখকের pk (প্রাইমারি কী) নির্দেশ করে।
# Subquery: expensive_books লেখকদের জন্য সেই বইগুলোর তালিকা তৈরি করে, যেগুলোর দাম ৫০
