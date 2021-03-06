from rest_framework import serializers
from .models import Food, Personal_Expenses, Insurance, Transportation, Housing, Utilities

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'restaurant', 'groceries', 'food_date', 'user_id']
        
class PersonalExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_Expenses
        fields = ['id', 'hobbies', 'clothes', 'streaming_services', 'subscriptions', 'expense_date', 'user_id']
        
class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ['id', 'home_insurance', 'auto_insurance', 'life_insurance', 'insurance_date', 'user_id']
        
class TransportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportation
        fields = ['id', 'auto_payment', 'fuel','public_transportation', 'auto_maintenance', 'transportation_date', 'user_id']
        
class HousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housing
        fields = ['id', 'rent', 'mortgage', 'property_tax', 'hoa', 'maintenance', 'housing_date', 'user_id']
        
class UtilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilities
        fields = ['id', 'water', 'electricity', 'hvac', 'gas', 'sewage', 'internet', 'phone', 'utilities_date', 'user_id']