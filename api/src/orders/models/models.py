from django.db import models
from api.src.profiles.models import Customer

# Create your models here.
class Orders(models.Model):
    item_name = models.CharField(max_length=80, unique=False, blank=False)
    amount = models.DecimalField(max_digits=12, unique=False, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
