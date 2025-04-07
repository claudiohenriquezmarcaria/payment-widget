from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
    mid = models.IntegerField(null=False, default=0);


class CreditCard(models.Model):
    number = models.CharField(max_length = 16)
    expiration = models.CharField(max_length = 5)
    cvc = models.CharField(max_length = 3)
    holder = models.CharField(max_length = 100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_creditcards',default=-1)

    def __str__(self):
        return self.number + " - " + self.expiration



class Transaction(models.Model):
    order = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)

