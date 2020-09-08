from django.db import models

# Create your models here.
class Bids(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    confirm = models.BooleanField()

    class Meta:
      verbose_name = 'bid'
      verbose_name_plural = 'bids'


    def __str__(self):
      return self.amount
