from django.contrib.auth.models import AbstractUser
from django.db import models
from unicodedata import decimal


# Create your models here.
class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_CHOICES = (
        ("expense", "Expense"),
        ("income", "Income"),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TRANSACTION_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount =  models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.type} of {self.amount} on {self.date} by {self.user}"