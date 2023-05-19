from django.db import models
from users.models import User
from products.models import Product

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    description = models.CharField(max_length=512)

    def __str__(self):
        return "id: " + str(self.id) + " product: " + str(self.product) + " username: " + str(self.username) + " description: " + self.description
    
