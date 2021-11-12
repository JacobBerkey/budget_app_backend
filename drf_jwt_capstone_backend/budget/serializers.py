from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'restaurant', 'groceries', 'user_id']
        
class PersonalExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'hobbies', 'clothes', 'streaming_services', 'subscriptions', 'user_id']
        
class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'home_insurance', 'auto_insurance', 'life_insurance', 'user_id']
        
class TransportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'auto_payment', 'fuel','public_transportation', 'auto_maintenance', 'user_id']
        
class HousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'rent', 'mortgage', 'property_tax', 'hoa', 'maintenance', 'user_id']
        
class UtilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'water', 'electricity', 'havac', 'gas', 'sewage', 'internet', 'phone', 'user_id']