duplicates = User.objects.values(
    'first_name'
    ).annotate(first_name_count=Count('first_name')).filter(first_name_count__gt=1)


for duplicate in duplicates:
    print(f"First Name: {duplicate['first_name']}, Count: {duplicate['first_name_count']}")
