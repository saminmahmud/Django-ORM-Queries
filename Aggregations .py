# Django-তে Aggregations হল একটি উপায় যা আপনাকে ডাটাবেস থেকে পরিসংখ্যানগত তথ্য সংগ্রহ করতে দেয়। এটি সাধারণত annotate(), aggregate(), এবং values() মেথডের মাধ্যমে করা হয়। এই পদ্ধতিগুলি ব্যবহার করে আপনি বিভিন্ন পরিসংখ্যান যেমন গড়, সর্বাধিক, সর্বনিম্ন, মোট এবং গণনা করতে পারেন।
# aggregate() ব্যবহার করে, আপনি একটি queryset-এর ওপর সাধারণভাবে ডেটার পরিসংখ্যান বের করেন, যেমন মোট সংখ্যা, গড়, সর্বোচ্চ বা সর্বনিম্ন মান ইত্যাদি।


# 1. aggregate() পদ্ধতি ব্যবহার করে আপনি একটি QuerySet এর উপর একটি বা একাধিক Aggregation ফাংশন প্রয়োগ করতে পারেন।

# উদাহরণস্বরূপ, ধরুন আপনার কাছে একটি Book মডেল আছে এবং আপনি বইয়ের সংখ্যা এবং গড় মূল্য বের করতে চান:
from django.db.models import Count, Avg

result = Book.objects.aggregate(total_books=Count('id'), average_price=Avg('price'))
print(result)  # {'total_books': 10, 'average_price': 15.50}


# 2. annotate() পদ্ধতি ব্যবহার করে আপনি প্রতিটি অবজেক্টের সাথে Aggregated মান যোগ করতে পারেন। এটি সাধারণত একটি গ্রুপিংয়ের সাথে ব্যবহৃত হয়।
from django.db.models import Count

authors_with_books = Author.objects.annotate(num_books=Count('book')).filter(num_books__gt=0)
for author in authors_with_books:
    print(f"{author.name} has written {author.num_books} books.")


# 3. values() পদ্ধতি ব্যবহার করে আপনি নির্দিষ্ট ফিল্ডের ভিত্তিতে Aggregation করতে পারেন।
book_prices = Book.objects.values('author').annotate(total_price=Sum('price'))
for item in book_prices:
    print(f"Author ID {item['author']} has a total book price of {item['total_price']}.")


# Aggregation ফাংশনগুলোর কিছু উদাহরণ :
# Count: রেকর্ডের সংখ্যা গণনা করতে।
# Sum: একটি ফিল্ডের মোট মান বের করতে।
# Avg: গড় মান বের করতে।
# Max: সর্বাধিক মান বের করতে।
# Min: সর্বনিম্ন মান বের করতে।



# >>> from django.db.models import Avg, Max, Min, Sum, Count
# >>> User.objects.all().aggregate(Avg('id'))
# {'id__avg': 7.571428571428571}
# >>> User.objects.all().aggregate(Max('id'))
# {'id__max': 15}
# >>> User.objects.all().aggregate(Min('id'))
# {'id__min': 1}
# >>> User.objects.all().aggregate(Sum('id'))
# {'id__sum': 106}