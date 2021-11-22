from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.DecimalField(max_digits=6, decimal_places=2)
    groceries = models.DecimalField(max_digits=6, decimal_places=2)
    food_date = models.DateField(auto_now_add=True)
    
class Personal_Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hobbies = models.DecimalField(max_digits=6, decimal_places=2)
    clothes = models.DecimalField(max_digits=6, decimal_places=2)
    streaming_services = models.DecimalField(max_digits=6, decimal_places=2)
    subscriptions = models.DecimalField(max_digits=6, decimal_places=2)
    expense_date = models.DateField(auto_now_add=True)
    
    
class Insurance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    home_insurance = models.DecimalField(max_digits=6, decimal_places=2)
    auto_insurance = models.DecimalField(max_digits=6, decimal_places=2)
    life_insurance = models.DecimalField(max_digits=6, decimal_places=2)
    insurance_date = models.DateField(auto_now_add=True)
    
    
class Transportation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auto_payment = models.DecimalField(max_digits=6, decimal_places=2)
    fuel = models.DecimalField(max_digits=6, decimal_places=2)
    public_transportation = models.DecimalField(max_digits=6, decimal_places=2)
    auto_maintenance = models.DecimalField(max_digits=6, decimal_places=2)
    transportation_date = models.DateField(auto_now_add=True)
    
    
class Housing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rent = models.DecimalField(max_digits=6, decimal_places=2)
    mortgage = models.DecimalField(max_digits=6, decimal_places=2)
    property_tax = models.DecimalField(max_digits=6, decimal_places=2)
    hoa = models.DecimalField(max_digits=6, decimal_places=2)
    maintenance = models.DecimalField(max_digits=6, decimal_places=2)
    housing_date = models.DateField(auto_now_add=True)
    

class Utilities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    water = models.DecimalField(max_digits=6, decimal_places=2)
    electricity = models.DecimalField(max_digits=6, decimal_places=2)
    hvac = models.DecimalField(max_digits=6, decimal_places=2)
    gas = models.DecimalField(max_digits=6, decimal_places=2)
    sewage = models.DecimalField(max_digits=6, decimal_places=2)
    internet = models.DecimalField(max_digits=6, decimal_places=2)
    phone = models.DecimalField(max_digits=6, decimal_places=2)
    utilities_date = models.DateField(auto_now_add=True)
    
