from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductCategory

def getproductscategorys(request):
    if request.method == 'GET':
        all = ProductCategory.objects.all()
        answer = []
        for product in all:
            answer.append({
                "id" : product.id,
                "name" : product.name,
                "image" : str(product.image)
            })
        return JsonResponse({'code': 200, 'answer': answer})
    return JsonResponse({'code': 405, 'answer': 'You need to use GET'})