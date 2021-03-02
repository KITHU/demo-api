from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.src.authentication.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country_code=models.IntegerField(null=True, blank=True)
    phone_no=models.IntegerField(null=True, blank=True)

    def __str__(self): 
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
    instance.customer.save()
