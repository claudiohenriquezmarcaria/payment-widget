from django.contrib import admin
from core.models import CreditCard, User, Transaction
# Register your models here.

admin.site.register(CreditCard)
admin.site.register(User)
admin.site.register(Transaction)
