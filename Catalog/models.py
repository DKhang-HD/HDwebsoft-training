from django.db import models

# Create your models here.


class Category(models.Model):
    type = models.CharField(max_length=200)
    picture = models.ImageField(blank=True, upload_to='Catalog/Category/images')

    def __str__(self):
        return self.type

    @property
    def image_url(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url


class Product(models.Model):
    type = models.ManyToManyField(Category)
    name = models.CharField(max_length=200)
    picture = models.ImageField(blank=True, upload_to='Catalog/Product/images')
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=30, null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url


class Order(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
