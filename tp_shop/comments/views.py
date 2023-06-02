from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Comment
from .serializers import CommentSerializer, CommentAddSerializer, CommentDeleteSerializer
from rest_framework import generics, status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import Product



class CommentListView(APIView):
    def get(self, request):
        """
                                            Получить все комментарии
                        """
        comment = Comment.objects.all()
        comments = []
        for comm in comment:
            comments.append({
                "id": comm.id,
                "product": comm.product,
                "username": comm.username,
                "description": comm.description
            })
        return Response({"code": 200, "answer": comments})


class CommentView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_QUERY, description='id',
                              type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request):
        """
                                                    Получить комментарий по id комментария
                                """
        id = request.GET.get("id")
        comments = Comment.objects.filter(id=id)
        if comments:
            comment = comments.first()
            data = {
                "id": comment.id,
                "product": comment.product,
                "username": comment.username,
                "description": comment.description
            }
            return Response({"code": 200, "answer": data})
        else:
            return Response({'code': 404, 'answer': 'Comment not found'})

class CreateCommentView(CreateAPIView):
    """
                                    Добавить комментарий
                """
    serializer_class = CommentAddSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            comment = Comment()
            comment.username = serializer.validated_data["username"]
            comment.product = serializer.validated_data["product"]
            comment.description = serializer.validated_data["description"]
            product_id = serializer.validated_data["product_id"]
            comment.save()
            products = Product.objects.filter(id=product_id)
            for product in products:
                product.comments += str(comment.id) + ","
                product.save()
            answer = {
                "id": comment.id,
                "product": comment.product,
                "username": comment.username,
                "description": comment.description
            }
        return Response({"code": 200, "answer": answer})


class DeleteCommentView(CreateAPIView):
    serializer_class = CommentDeleteSerializer
    def post(self, request):
        """
                                           Удалить комментарий
                        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            id = serializer.validated_data["id"]
            product_id = serializer.validated_data["product_id"]

            if id is None or product_id is None:
                return Response({"error": "Missing 'id' or 'product_id' in request data"},
                                status=status.HTTP_400_BAD_REQUEST)

            products = Product.objects.filter(id=product_id)
            for product in products:
                product.comments = product.comments.replace(str(id) + ',', '')
                product.save()

            try:
                comment = Comment.objects.get(id=id)
                comment.delete()
            except Comment.DoesNotExist:
                return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"code": 200, "answer": "Delete"}, status=status.HTTP_200_OK)
