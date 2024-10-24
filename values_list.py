# values_list() ব্যবহার করে, আপনি একইভাবে ফিল্টারিং করতে পারেন, কিন্তু ফলাফল টিউপল বা তালিকা আকারে থাকবে।


from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


# এখন ধরুন, আমরা ৫০-এর নিচে দাম বিশিষ্ট পণ্যগুলোর নাম এবং দাম পেতে চাই।
products = Product.objects.filter(price__lt=50).values_list('name', 'price')

for product in products:
    print(f"Product Name: {product[0]}, Price: {product[1]}")

