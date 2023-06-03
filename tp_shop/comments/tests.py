from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.urls import reverse
from .models import Comment
from .serializers import CommentAddSerializer, CommentDeleteSerializer
from .views import CommentListView, CommentView, CreateCommentView, DeleteCommentView

class CommentListViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_all_comments(self):
        # Создаем несколько комментариев для теста
        Comment.objects.create(product="Product 1", username="User 1", description="Comment 1")
        Comment.objects.create(product="Product 2", username="User 2", description="Comment 2")

        # Создаем GET-запрос
        url = reverse('getcommentslist')
        request = self.factory.get(url)
        view = CommentListView.as_view()

        # Отправляем запрос и получаем ответ
        response = view(request)

        # Проверяем код ответа и данные
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['answer']), 2)  # Проверяем, что получили два комментария

class CommentViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_comment_by_id(self):
        # Создаем комментарий для теста
        comment = Comment.objects.create(product="Product 1", username="User 1", description="Comment 1")

        # Создаем GET-запрос с параметром id
        url = reverse('getcomment')
        request = self.factory.get(url, {'id': comment.id})
        view = CommentView.as_view()

        # Отправляем запрос и получаем ответ
        response = view(request)

        # Проверяем код ответа и данные
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['answer']['id'], comment.id)

class CreateCommentViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_create_comment(self):
        # Создаем POST-запрос с данными для создания комментария
        url = reverse('post')
        data = {
            'product': 'Product 1',
            'username': 'User 1',
            'description': 'Comment 1',
            'product_id': 1
        }
        request = self.factory.post(url, data)
        view = CreateCommentView.as_view()

        # Отправляем запрос и получаем ответ
        response = view(request)

        # Проверяем код ответа и данные
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('id' in response.data['answer'])
        self.assertEqual(response.data['answer']['product'], 'Product 1')

class DeleteCommentViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_delete_comment(self):
        # Создаем комментарий для теста
        comment = Comment.objects.create(product="Product 1", username="User 1", description="Comment 1")

        # Создаем POST-запрос с данными для удаления комментария
        url = reverse('delete')
        data = {
            'id': comment.id,
            'product_id': 1
        }
        request = self.factory.post(url, data)
        view = DeleteCommentView.as_view()

        # Отправляем запрос и получаем ответ
        response = view(request)

        # Проверяем код ответа и данные
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['answer'], 'Delete')
        self.assertFalse(Comment.objects.filter(id=comment.id).exists())