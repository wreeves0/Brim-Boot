from django.db import models

# Create your models here.
class BinVO(models.model):
    import_href = models.CharField(max_length=200 , unique=True)
