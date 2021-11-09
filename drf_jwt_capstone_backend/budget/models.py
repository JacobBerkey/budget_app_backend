from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.DecimalField(max_digits=6, decimal_places=2)
    groceries = models.DecimalField(max_digits=6, decimal_places=2)
