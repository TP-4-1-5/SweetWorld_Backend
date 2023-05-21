from django.db import models

class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    favorites = models.CharField(max_length=100, default='0,')

    def __str__(self):
        return 'id: ' + str(self.id) +  ' username: ' + self.username + ' password: ' + self.password + '<br>'
