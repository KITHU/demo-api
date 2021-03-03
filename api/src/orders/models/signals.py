from django.db.models.signals import post_save
from django.dispatch import receiver
from api.src.orders.models.models import Orders
from api.src.orders.sms import send_sms

@receiver(post_save, sender=Orders)
def sendSmsNotifications(instance, **kwargs):
    product = instance.item_name
    username = instance.customer.user.username
    amount = str(instance.amount)
    message = "Dear {}, your order for {} valued at {} has been placed.".format(username,product,amount)
    mobile = "+"+str(instance.customer.country_code)+str(instance.customer.phone_no)
   

    send_sms(message, mobile)
