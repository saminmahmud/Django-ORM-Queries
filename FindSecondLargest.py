# Though the ORM gives the flexibility of finding first(), last() item from the queryset but not nth item. You can do it using the slice operator.

user = User.objects.order_by('-last_login')[2] # Third Highest record w.r.t 'last_login'

