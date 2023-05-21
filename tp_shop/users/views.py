import json

from users.models import User
from django.http import JsonResponse

from django.contrib.auth.models import User as user2


def registration(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = json_data["username"]
        password = json_data["password"]
        if (len(password) >= 8 and len(username) > 0):
            for user in User.objects.all():
                if username == user.username:
                    return JsonResponse({
                        'code': 400,
                        'answer': 'A user with the same name already exists'
                    })
            user = User.objects.create(username=username, password=password)
            user.save()
            return JsonResponse({
                'code': 200,
                'id': user.id,
                'username': user.username,
                'password': user.password
            })
        return JsonResponse({'code': 400, 'answer': 'password length must be greater than 8, username 0'})
    return JsonResponse({'code': 405, 'answer': 'You need to use POST'})


def login(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = json_data["username"]
        password = json_data["password"]
        user1 = []
        for user in User.objects.all():
            if (password == user.password) and (username == user.username):
                user1 = user
                is_superuser1 = False
                for user3 in user2.objects.filter(is_superuser=True):
                    is_superuser1 = is_superuser1 or (user3.username==user1.username)
                return JsonResponse({"code" : 200, "answer": {
                    "username" : user1.username,
                    "password" : user1.password,
                    "is_superuser" : is_superuser1
                }})
        return JsonResponse({'code': 401, 'answer': 'login/paswword incorrectly'})
    return JsonResponse({'code': 405, 'answer': 'You need to use POST'})


def getFavorites(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        for user in User.objects.all():
            if username == user.username:
                answer = user.favorites.split(",")
                answer = list(map(int, answer[1:len(answer)-1]))
                return JsonResponse({'code': 200, 'answer': answer})
        return JsonResponse({'code': 500, 'answer': 'something went wrong, try to relogin'})
    return JsonResponse({'code': 405, 'answer': 'You need to use GET'})
