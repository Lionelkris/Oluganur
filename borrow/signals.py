from django.db.models.signals import post_save
from .models import Lenders
from django.dispatch import receiver
from .models import LenderProfile


@receiver(post_save, sender=Lenders)
def create_profile(sender, instance, created, **kwargs):
    if created:
        LenderProfile.objects.create(lender=instance)


@receiver(post_save, sender=Lenders)
def save_profile(sender, instance, **kwargs):
    instance.lenderprofile.save()
