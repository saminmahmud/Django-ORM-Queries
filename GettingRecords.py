# objects.all() ব্যবহার করে আপনি একটি মডেলের সব রেকর্ড সহজে পেতে পারেন।
# এটি একটি QuerySet ফেরত দেয় যা পরে আপনার প্রয়োজন অনুযায়ী ব্যবহার করা যায়।


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


# আপনি যদি Product মডেলের সমস্ত পণ্য দেখতে চান, তাহলে:
products = Product.objects.all()

for product in products:
    print(f"Product Name: {product.name}, Price: {product.price}")


# (ID) দ্বারা
person = Person.objects.get(id=1)
# (Multiple)
person = Person.objects.get(first_name='John', last_name='Doe')



# get() ব্যবহার করুন যখন আপনি একক অবজেক্ট প্রয়োজন এবং আপনি তার বিশেষত্ব সম্পর্কে নিশ্চিত।
# filter() ব্যবহার করুন যখন আপনি একাধিক অবজেক্ট বা শূন্য অবজেক্ট পাওয়ার সম্ভাবনা রয়েছে এবং সেইসব ক্ষেত্রে পরিচালনা করতে চান।