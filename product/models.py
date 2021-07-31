from django.db import models

# Create your models here.

class Product(models.Model) :
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    info = models.CharField(max_length=10000)
    price = models.IntegerField()
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name