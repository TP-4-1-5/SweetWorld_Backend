from django.http import JsonResponse
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProductCategory
from .serializers import ProductCategorySerializer


class ProductCategoryView(APIView):
    def get(self, request):
        """
        Получить список категорий
        """
        if request.method == 'GET':
            all = ProductCategory.objects.all()
            answer = []
            for product in all:
                answer.append({
                    "id": product.id,
                    "name": product.name,
                    "image": str(product.image)
                })
            return JsonResponse({'code': 200, 'answer': answer})
        return JsonResponse({'code': 405, 'answer': 'You need to use GET'})