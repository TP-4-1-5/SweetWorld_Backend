from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Product
from users import models


def getproduct(request):
    if request.method == "GET":
        id = int(request.GET.get("id"))
        for product in Product.objects.all():
            if product.id == id:
                return JsonResponse({'code': 200, 'answer': {
                    "id": product.id,
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                    "image": str(product.image),
                    "category": str(product.category.name),
                }})
        return JsonResponse({'code': 400, 'answer': 'Product with this id do not exist'})
    return JsonResponse({'code': 405, 'answer': 'You need to use GET'})


def getproductlist(request):
    if request.method == "GET":
        all = Product.objects.all().order_by('id')
        answer = {}
        num = 1
        page = 1
        page_body = []
        for product in all:
            page_body.append({
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "image": str(product.image),
                "category": str(product.category.name),
            })
            num += 1
            if num == 10:
                num = 1
                answer.update({page: page_body})
                page += 1
                page_body = []
        if len(page_body) != 0:
            answer.update({page: page_body})
        return JsonResponse({'code': 200, "answer": answer})
    return JsonResponse({'code': 405, 'answer': 'You need to use GET'})


def getproductlistwithcategory(request):
    if request.method == "GET":
        id = int(request.GET.get('id'))
        productss = Product.objects.all()
        products = []
        for product in productss:
            if product.category.id == id:
                products.append(product)
        answer = {}
        num = 1
        page = 1
        page_body = []
        for product in products:
            page_body.append({
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "image": str(product.image),
                "category": str(product.category.name),
            })
            num += 1
            if num == 10:
                num = 1
                answer.update({page: page_body})
                page += 1
                page_body = []
        if len(page_body) != 0:
            answer.update({page: page_body})
        return JsonResponse({'code': 200, "answer": answer})
    return JsonResponse({'code': 405, 'answer': 'You need to use GET'})


def addtofavorite(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        username = json_data["username"]
        id = json_data['id']
        users = models.User.objects.filter(username=username)
        for user in users:
            if str(id) in user.favorites.split(','):
                return JsonResponse({'code': 400, 'answer': "already in favorites"})
            user.favorites += (str(id) + ',')
            user.save()
            return JsonResponse({"code": 200, 'answer': str(user.favorites)})
    return JsonResponse({'code': 405, 'answer': 'You need to use POST'})


def deletefromfavorite(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        username = json_data["username"]
        id = json_data['id']
        users = models.User.objects.filter(username=username)
        for user in users:
            user.favorites = user.favorites.replace(str(id) + ',', '')
            user.save()
            return JsonResponse({"code": 200, 'answer': str(user.favorites)})
    return JsonResponse({'code': 405, 'answer': 'You need to use POST'})

def getcommentslist(request):
    if request.method == "GET":
        id = int(request.GET.get("id"))
        products = Product.objects.filter(id=id)
        for product in products:
            answer = product.comments.split(",")
            answer = list(map(int, answer[1:len(answer) - 1]))
            return JsonResponse({"code": 200, "answer": answer})
    return JsonResponse({'code': 405, 'answer': 'You need to use GET'})


def getproductlistwithname(request):
    if request.method == "GET":
        name = request.GET.get('name')
        productss = Product.objects.all()
        products = []
        for product in productss:
            if name in product.name:
                products.append(product)
        answer = {}
        num = 1
        page = 1
        page_body = []
        for product in products:
            page_body.append({
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "image": str(product.image),
                "category": str(product.category.name),
            })
            num += 1
            if num == 10:
                num = 1
                answer.update({page: page_body})
                page += 1
                page_body = []
        if len(page_body) != 0:
            answer.update({page: page_body})
        return JsonResponse({'code': 200, "answer": answer})
    return JsonResponse({'code': 405, 'answer': 'You need to use GET'})


