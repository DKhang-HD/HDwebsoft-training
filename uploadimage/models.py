from django.db import models
# Create your models here.


class UploadImage(models.Model):
	name = models.CharField(max_length=50)
	image_file = models.ImageField(upload_to='uploadimage/UploadImage/images/')			# media folder is default selected
