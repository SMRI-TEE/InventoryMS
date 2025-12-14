from rest_framework import serializers
from .models import Product,ProductCategory,ProductDepartment,ProductPurchase,ProductSell
# object data lie json ma convert garni or json lie object ma convert garni 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ['name',''] for particular field.
        fields = '__all__'
        
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory    
        fields = '__all__' 