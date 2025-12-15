from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from .models import Product,ProductCategory
from .serializers import ProductSerializer,ProductCategorySerializer
from rest_framework.response import Response
# Create your views here.
 
class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
     
         
class ProductCategoryApiView(GenericViewSet):
    queryset = ProductCategory.objects.all()  
    serializer_class = ProductCategorySerializer
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)    
        
    def list(self,rewuest):
        queryset = self.get_queryset()
                 