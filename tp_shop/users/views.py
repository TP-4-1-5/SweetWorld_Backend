import json
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from drf_yasg import openapi
from .models import User
from .serializers import UserSerializer, UserLogin, UserSignUp, UserFavoriteSerializer
from .models import User as user2
from rest_framework import generics
from rest_framework.views import APIView


class RegistrationView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSignUp
    # permission_classes = [AllowAny]
    def post(self, request):
        """
        Регистрация нового пользователя
        """
        if request.method == 'POST':
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                username = serializer.validated_data.get('username')
                password = serializer.validated_data.get('password')

                existing_user = User.objects.filter(username=username).exists()
                if existing_user:
                    return Response({
                        'code': 400,
                        'answer': 'A user with the same name already exists'
                    }, status=status.HTTP_400_BAD_REQUEST)

                user = User.objects.create(username=username, password=password)
                return Response(self.serializer_class(user).data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'code': 405, 'answer': 'You need to use POST'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class LoginView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLogin

    def post(self, request):
        """
        Авторизация пользователя
        """
        if request.method == 'POST':
            json_data = json.loads(request.body)
            username = json_data["username"]
            password = json_data["password"]
            user1 = []
            for user in User.objects.all():
                if (password == user.password) and (username == user.username):
                    user1 = user
                    return JsonResponse({"code": 200, "answer": {
                        "username": user1.username,
                        "password": user1.password,
                    }})
            return JsonResponse({'code': 401, 'answer': 'login/paswword incorrectly'})
        return JsonResponse({'code': 405, 'answer': 'You need to use POST'})


class FavoritesView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('username', openapi.IN_QUERY, description='username',
                              type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request):
        """
        Получить список избранного по имени пользователя
        """
        if request.method == 'GET':
            username = request.GET.get('username')
            for user in User.objects.all():
                if username == user.username:
                    answer = user.favorites.split(",")
                    answer = list(map(int, answer[1:len(answer)-1]))
                    return Response({'code': 200, 'answer': answer})
            return Response({'code': 500, 'answer': 'something went wrong, try to relogin'})
        return Response({'code': 405, 'answer': 'You need to use GET'})

