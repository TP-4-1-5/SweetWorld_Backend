from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer, ProductAddFavoriteSerializer, ProductViewSerializer, \
    ProductDeleteFavoriteSerializer
from .models import Product
from .serializers import ProductSerializer
from users.models import User
from comments.serializers import CommentSerializer
from users.serializers import UserSerializer
from users.serializers import UserUsernameSerializer



class ProductView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_QUERY, description='id', type=openapi.TYPE_INTEGER, default=1),
        ]
    )
    def get(self, request):
        """
                        Получить информацию о продукте по id продукта
                """
        id = int(request.GET.get("id"))
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response({'code': 200, 'answer': serializer.data})
        except Product.DoesNotExist:
            return Response({'code': 400, 'answer': 'Product with this id does not exist'})



class ProductListView(APIView):
    def get(self, request):
        """
                        Получить информацию о всех продуктах
                """
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



class ProductListWithCategoryView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_QUERY, description='id', type=openapi.TYPE_INTEGER, default=1),
        ]
    )
    def get(self, request):
        """
                Получить информацию о продукте по id категории
        """
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



class AddToFavoritesView(CreateAPIView):
    """
                                   Добавить продукт в избранное
                """
    serializer_class = ProductAddFavoriteSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            id = serializer.validated_data['id']
            users = User.objects.filter(username=username)
            for user in users:
                if str(id) in user.favorites.split(','):
                    return JsonResponse({'code': 400, 'answer': "already in favorites"})
                user.favorites += (str(id) + ',')
                user.save()
                return JsonResponse({"code": 200, 'answer': str(user.favorites)}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeleteFromFavoritesView(CreateAPIView):
    serializer_class = ProductDeleteFavoriteSerializer
    def post(self, request):
        """
                                       Удалить продукт из избранного
                    """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            id = serializer.validated_data['id']
            users = User.objects.filter(username=username)
            for user in users:
                user.favorites = user.favorites.replace(str(id) + ',', '')
                user.save()
                return JsonResponse({"code": 200, 'answer': str(user.favorites)})
        return JsonResponse({'code': 405, 'answer': 'You need to use POST'})



class GetProductComments(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_QUERY, description='id',
                              type=openapi.TYPE_STRING, default=1),
        ]
    )
    def get(self, request):
        """
                                Получить id комментария по id продукта
            """
        if request.method == "GET":
            id = int(request.GET.get("id"))
            products = Product.objects.filter(id=id)
            for product in products:
                answer = product.comments.split(",")
                answer = list(map(int, answer[1:len(answer) - 1]))
                return JsonResponse({"code": 200, "answer": answer})
        return JsonResponse({'code': 405, 'answer': 'You need to use GET'})



class ProductListWithNameView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY, description='name',
                              type=openapi.TYPE_STRING, default='vaflya'),
        ]
    )
    def get(self, request):
        """
        Получить информацию о продукте по названию продукта
        """
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