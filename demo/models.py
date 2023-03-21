from django.db import models
#sqlalchemy
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    color = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name# вместо Class 243423.. будет выводиться на экран строка, но обязательно значение строчное!

    def __repr__(self):
        return self.name