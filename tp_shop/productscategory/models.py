from django.db import models

class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=128)
    image = models.ImageField(upload_to='productscategory_image')

    def __str__(self):
        return 'id: ' + str(self.id) + ' name: ' + self.name + ' image: ' + str(self.image)
