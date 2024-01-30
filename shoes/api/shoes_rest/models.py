from django.db import models

# Create your models here.

class BinVO(models.Model):
    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()



class Shoe(models.Model):
   manufacturer = models.CharField(max_length=200)
   model_name = models.CharField(max_length=200)
   color = models.CharField(max_length=200)
   picture_url = models.URLField(null=True)
