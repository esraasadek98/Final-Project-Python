from urllib import request
from .serializers import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework .parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics,filters
import os

# Create your views here.

@csrf_exempt
def Create_User(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def check_login(request,email):
    try:
        user = User.objects.filter(email=email)
    except:
        return HttpResponse(status=404)


    if request.method == 'GET':
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def get_user(request,id):
    try:
        user = User.objects.get(pk=id)
    except:
        return HttpResponse(status=404)


    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)



@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products=Product.objects.all().order_by('create_at').reverse()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def product_by_id(request, pk):
    try:
      product = Product.objects.get(pk=id)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=201)

@csrf_exempt
def product_seller(request, storeId):
    try:
      product = Product.objects.get(storeId=storeId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def productImg_list(request):
    if request.method == 'GET':
        productImgs = ProductImg.objects.all()
        serializer = ProductImgSerializer(productImgs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)





  
      
    

    
   