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
        
    def list(self,request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk):
        # queryset = ProductCategory.objects.get(id=pk)
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
                 
    def update(self,request,pk):
        queryset = self.get_object() # id anusar data lauxa.
        serializer = self.get_serializer(queryset,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def partial_update(self,request,pk):
        queryset = self.get_object() # id anusar data lauxa.
        serializer = self.get_serializer(queryset,data=request.data,partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  
        
    def destroy(self,request,pk):
        queryset = self.get_object()
        queryset.delete()
        return Response()                  