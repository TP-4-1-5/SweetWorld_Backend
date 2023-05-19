from django.shortcuts import render
from .models import Comment
from django.http import JsonResponse
import json
from products.models import Product

def getcommentslist(request):
    if request.method == "GET":
        comment = Comment.objects.all()
        comments = []
        for comm in comment:
            comments.append({
                "id": comm.id,
                "product": comm.product,
                "username": comm.username,
                "description": comm.description
            })
        return JsonResponse({"code": 200, "answer": comments})
    return JsonResponse({'code': 405, 'answer': 'You need to use GET'})

def getcomment(request):
    if request.method == "GET":
        id = request.GET.get("id")
        comments = Comment.objects.filter(id=id)
        for comment in comments:
            return JsonResponse({"code": 200, "answer": {
                "id": comment.id,
                "product": comment.product,
                "username": comment.username,
                "description": comment.description
            }})
    return JsonResponse({'code': 405, 'answer': 'You need to use GET'})

def post(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        comment = Comment()
        comment.username = json_data["username"]
        comment.product = json_data["product"]
        comment.description = json_data["description"]
        product_id = json_data["product_id"]
        comment.save()
        products = Product.objects.filter(id=product_id)
        for product in products:
            product.comments += str(comment.id) + ","
            product.save()
        answer = {
            "id" : comment.id,
            "product" : comment.product,
            "username" : comment.username,
            "description" : comment.description
        }
        return JsonResponse({"code": 200, "answer": answer})
    return JsonResponse({'code': 405, 'answer': 'You need to use POST'})

def delete(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        id = json_data["id"]
        product_id = json_data["product_id"]
        products = Product.objects.filter(id=product_id)
        for product in products:
            product.comments = product.comments.replace(str(id)+',', '')
            product.save()
        Comment.objects.get(id = id).delete()
        return JsonResponse({"code": 200, "answer": "Delete"})
    return JsonResponse({'code': 405, 'answer': 'You need to use POST'})
