# Django-তে Q objects ব্যবহার করা হয় জটিল কুয়েরি তৈরি করতে। এটি বিশেষ করে যখন আপনাকে অ্যান্ড (AND) এবং অর (OR) শর্ত একসাথে ব্যবহার করতে হয়। 
# Q objects আপনাকে একাধিক শর্তের ভিত্তিতে ডাটাবেজ থেকে তথ্য নির্বাচন করতে সাহায্য করে। এটি আপনাকে শর্তগুলোকে একত্রিত করতে দেয়, যাতে আপনি কুয়েরি আরও জটিল করতে পারেন।


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)


# যদি আমরা দেখতে চাই যে পণ্যগুলোর দাম ৫০-এর কম অথবা তারা স্টকে আছে:
from django.db.models import Q

products = Product.objects.filter(Q(price__lt=50) | Q(is_available=True))

for product in products:
    print(product.name)


# আপনি যদি দেখতে চান পণ্যের দাম ৫০ এর বেশি এবং তা স্টকে আছে:
products = Product.objects.filter(Q(price__gt=50) & Q(is_available=True))

for product in products:
    print(product.name)


# আপনি Q objects ব্যবহার করে জটিল শর্তও তৈরি করতে পারেন। ধরুন, আপনি চান যে পণ্যগুলোর দাম ৫০ এর কম, এবং একই সাথে স্টক যদি ১০০-এর বেশি হয় অথবা মূল্য যদি ১০০ এর বেশি হয়।
products = Product.objects.filter(
    Q(price__lt=50) & Q(stock__gt=100) | Q(price__gt=100)
)


# এভাবে আপনি Django-তে Q objects ব্যবহার করে আপনার কুয়েরিগুলোকে আরও শক্তিশালী এবং নমনীয় করতে পারেন।
