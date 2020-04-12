from django.db import models
from django.utils import timezone
from PIL import Image


class LenderTypes(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Lenders(models.Model):
    title = models.CharField(max_length=200)
    lender_type = models.ForeignKey(LenderTypes, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class LenderPreferences(models.Model):
    trading_years = models.FloatField(default=0.0)
    turnover_per_year_in_thousands = models.FloatField(default=0.0)
    machine_vehicle_purchase = models.BooleanField(default=False)
    purchases_with_min_outstanding_in_thousands = models.FloatField(default=0.0)
    debit_credit_card_payment_txn = models.FloatField(default=0.0)
    lender_id = models.ForeignKey(Lenders, on_delete=models.CASCADE)
    lender_type = models.ForeignKey(LenderTypes, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lender_type) + " " + str(self.lender_id)


class LenderProfile(models.Model):
    lender = models.OneToOneField(Lenders, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.lender.title} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

