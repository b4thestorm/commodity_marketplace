from django.db import models
from django.contrib.auth.models import (AbstractBaseUser)
from django.contrib.auth.models import (User)

# Create your models here.
class Bids(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    confirm = models.BooleanField()
    seller = models.ForeignKey(User, related_name="seller", on_delete=models.CASCADE, default=None)
    buyer = models.ForeignKey(User, related_name="buyer",   on_delete=models.CASCADE, default=None)

    class Meta:
      verbose_name = 'bid'
      verbose_name_plural = 'bids'


    def __str__(self):
      return self.amount


class User(AbstractBaseUser):
  USER_TYPE_CHOICES = (
      (1, 'seller'),
      (2, 'buyer'),
    )
  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
