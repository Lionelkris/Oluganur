from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserRequestProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=200)
    borrower_trade_years = models.FloatField(default=0.0)
    borrower_turnover_yearly = models.FloatField(default=0.0)
    borrower_machine_vehicle_purchase = models.BooleanField(default=False)
    borrower_purchases_with_min_outstanding_in_thousands = models.FloatField(default=0.0)
    debit_credit_card_payment_txn = models.FloatField(default=0.0)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Request Profile'
