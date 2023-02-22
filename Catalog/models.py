from django.db import models

# Create your models here.


class Category(models.Model):
    type_book = models.CharField(max_length=200)

    def __str__(self):
        return self.type_book


class Product(models.Model):
    type_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_book = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name_book
