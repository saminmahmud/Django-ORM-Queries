# values() মেথড ব্যবহার করে আপনি নির্দিষ্ট ক্ষেত্রের মান ডিকশনারি আকারে ফেরত পান। ফিল্টারিং করার সময়, আপনি চাইলে নির্দিষ্ট শর্ত দিয়ে QuerySet তৈরি করতে পারেন।


from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


# এখন ধরুন, আমরা ৫০-এর নিচে দাম বিশিষ্ট পণ্যগুলোর নাম এবং দাম পেতে চাই।
products = Product.objects.filter(price__lt=50).values('name', 'price')

for product in products:
    print(f"Product Name: {product['name']}, Price: {product['price']}")
