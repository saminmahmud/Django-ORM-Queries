# F Expressions আপনাকে একটি মডেলের ক্ষেত্রের মানের সাথে অন্যান্য ক্ষেত্রের মান ব্যবহার করে গণনা করতে দেয়। উদাহরণস্বরূপ, আপনি একটি ক্ষেত্রের মান বাড়াতে বা কমাতে চাইলে F Expression ব্যবহার করতে পারেন।
# F Expressions: একাধিক ক্ষেত্রের মানের সাথে গণনা করতে সাহায্য করে।

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


# এখন, ধরুন আমরা সমস্ত পণ্যের দাম ১০% বাড়াতে চাই:
from django.db.models import F
# সব পণ্যের দাম ১০% বৃদ্ধি করুন
Product.objects.update(price=F('price') * 1.10)


# ধরি, আপনি সেই সমস্ত পণ্য দেখতে চান যেগুলোর স্টক ১০০ এর কম এবং দাম ৫০-এর বেশি:
products = Product.objects.filter(stock__lt=100, price__gt=50)

for product in products:
    print(product.name)


# ধরি, আমরা একটি নতুন ক্ষেত্র যোগ করতে চাই, যা total_value হিসাবে price * stock গণনা করবে:
from django.db.models import F, ExpressionWrapper, DecimalField

# নতুন total_value ক্ষেত্র তৈরি করুন
products = Product.objects.annotate(
    total_value=ExpressionWrapper(F('price') * F('stock'), output_field=DecimalField())
)

for product in products:
    print(f"{product.name}: Total Value = {product.total_value}")


# find the users where first_name==last_name
User.objects.filter(last_name=F("first_name"))
