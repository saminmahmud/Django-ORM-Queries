# Django-তে annotate() ফাংশন ব্যবহার করে আপনি আপনার queryset-এ নতুন ক্ষেত্র যুক্ত করতে পারেন, যা বিভিন্ন গণনা ফাংশনের ফলাফল ভিত্তিক।
# annotate(): নতুন ক্ষেত্র তৈরি করতে ব্যবহৃত হয়।


from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField()
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


from django.db.models import Count, Sum
from myapp.models import Author

# লেখক এবং তাদের বইয়ের সংখ্যা ও মোট পৃষ্ঠার সংখ্যা পান
authors_with_stats = Author.objects.annotate(
    book_count=Count('books'),            # বইয়ের সংখ্যা গুনুন
    total_pages=Sum('books__pages')       # মোট পৃষ্ঠার সংখ্যা গুনুন
)

# ফলাফল প্রদর্শন করুন
for author in authors_with_stats:
    print(f"{author.name} has written {author.book_count} books with a total of {author.total_pages} pages.")


# ব্যাখ্যা
# annotate(): এখানে annotate() ব্যবহার করে আমরা প্রতিটি লেখকের জন্য দুটি নতুন ক্ষেত্র যুক্ত করেছি:

# book_count: লেখকের বইয়ের সংখ্যা।
# total_pages: লেখকের সমস্ত বইয়ের মোট পৃষ্ঠার সংখ্যা।
# Count('books'): books সম্পর্কিত ক্ষেত্রের উপর ভিত্তি করে বইয়ের সংখ্যা গুনছে। এখানে related_name ব্যবহার করা হয়েছে, যা Book মডেলে সংজ্ঞায়িত হয়েছে।

# Sum('books__pages'): books সম্পর্কের মাধ্যমে pages ক্ষেত্রের মোট যোগফল বের করছে।
