from django.db import models
from productscategory import models as model

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="products_image")
    category = models.ForeignKey(to=model.ProductCategory, on_delete=models.CASCADE)
    comments = models.CharField(max_length=1024, default='0,')

    def __str__(self):
        return "id: " + str(self.id) + " name: " + self.name + " product_category: " + str(self.category)
