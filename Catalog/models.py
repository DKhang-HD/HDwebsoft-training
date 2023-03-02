from django.db import models
import uuid     # Required for unique book instances
from datetime import date
from User.models import MyUser
# Create your models here.


class Category(models.Model):
    type = models.CharField(max_length=200)
    picture = models.ImageField(blank=True, upload_to='Catalog/Category/images')

    class Meta:
        ordering = ['type']

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

    class Meta:
        ordering = ['name', 'price']

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url


class ProductInstance(models.Model):
    """Model representing a specific copy of a product (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular book across whole library')
    # RESTRICT: ensure Product can't be delete
    product = models.ForeignKey('Product', on_delete=models.RESTRICT, null=True)
    borrower = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.product.name})'

    @property
    def is_overdue(self):
        """Determines if the product is overdue based on due date and current date."""
        return bool(self.due_back and date.today() > self.due_back)

# class Work(models.Model):
#     category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
#     sales = models.IntegerField(null=True)
