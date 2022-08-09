from fileinput import filename
from telnetlib import STATUS
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
def create_user(request):
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
        product = Product.objects.get(pk=pk)
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
        serializer = ProductImgSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def productImg_product_Id(request,productId):
    try:
        productImg=ProductImg.objects.filter(productId=productId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductImgSerializer(productImg,many=True)
        return JsonResponse(serializer.data, safe=False)



@csrf_exempt
def productImg_by_Id(request,id):
    try:
        productImg=ProductImg.objects.get(pk=id)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductImgSerializer(productImg)
        return JsonResponse(serializer.data)
    elif request.method == 'DELETE':
        productImg.delete()
        return HttpResponse(status=201)


@csrf_exempt
def product_by_category(request,category):
    try:
        product=Product.objects.filter(category=category)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)



@csrf_exempt
def cart_list(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def cart_by_user_id(request,userId):
    try:
        cart=Cart.objects.filter(userId=userId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CartSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CartSerializer(cart, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        cart.delete()
        return HttpResponse(status=201)



@csrf_exempt
def cart_item_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CartItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def cartItem_by_id(request,pk):
    try:
        cardItem=CartItem.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CartItemSerializer(cardItem, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CartItemSerializer(cardItem, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        cardItem.delete()
        return HttpResponse(status=201)



@csrf_exempt
def cartItem_by_cart(request,cartId):
    try:
        cardItem=CartItem.objects.filter(cartId=cartId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CartItemSerializer(cardItem, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def cartItem_by_cart_id(request,cartId):
    try:
        cardItem=CartItem.objects.filter(cartId=cartId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CartItemSerializer(cardItem, many=True)
        return JsonResponse(serializer.data, safe=False)



@csrf_exempt
def cartItem_detect_same_product(request,cartId,productId):
    try:
        cardItem=CartItem.objects.filter(cartId=cartId).filter(productId=productId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CartItemSerializer(cardItem, many=True)
        return JsonResponse(serializer.data, safe=False)


class search_product(generics.ListAPIView):
    search_fields = ('title', 'description', 'category')
    filter_backends = (filter.SearchFilter)
    queryset = Product.objects.all()
    serializer_class= ProductSerializer


@csrf_exempt
def create_store(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def get_store(request,userId):
    try:
        store =Store.objects.filter(userId=userId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StoreSerializer(store, many=True)
        return JsonResponse(serializer.data, safe=False)


class upload_file(generics.CreateAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer


@csrf_exempt
def delete_file(request):
    if request.method == 'GET':
        ext = filename.split('.')[-1]
        filenamenoExt = filename.replace(f'{ext}',"" )
        fileDir = "%s/%s.%s"("img",filenamenoExt, ext)
        if os.path.isfile((f'{img}/{filename}')):
            os.remove(fileDir)
            return HttpResponse(f'{filename} deleted')
        return HttpResponse('file not found')

@csrf_exempt
def filter_range_price(request,minprice,maxprice):
    try:
        products =Product.objects.filter(price__range=(minprice,maxprice))
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def filter_min_price(request,minprice):
    try:
        products =Product.objects.filter(price__gte=minprice)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def filter_max_price(request,maxprice):
    try:
        products =Product.objects.filter(price__lte=maxprice)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def filter_rating(request,rating):
    try:
        products =Product.objects.filter(rating__gte= rating)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)



def filter_condition(request,condition):
    try:
        products =Product.objects.filter(condition= condition)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_price_and_rating(request,minprice,maxprice,rating):
    try:
        products =Product.objects.filter(price_range=(minprice,maxprice)).filter(rating_gte=rating)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_price_and_condition(request,minprice,maxprice,condition):
    try:
        products =Product.objects.filter(price_range=(minprice,maxprice)).filter(condition=condition)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_rating_and_condition(request,rating,condition):
    try:
        products =Product.objects.filter(rating_gte=rating).filter(condition=condition)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_all(request,minprice,maxprice,rating,condition):
    try:
        products =Product.objects.filter(price_range=(minprice,maxprice)).filter(rating_gte=rating).filter(condition=condition)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)



def get_cart_item_by_id(request,cartId):
    try:
        cartItem =CartItem.objects.filter(cartId=cartId).prefetch_related('productId').order_by('create_at')
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Joinserializer(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)
