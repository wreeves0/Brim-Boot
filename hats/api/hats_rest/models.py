from django.db import models

# Create your models here.


class LocationVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)

class Hat(models.Model):
    fabric = models.CharField(max_length=200)
    style_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    picture_url = models.URLField(null=True, blank=True)
    # location = models.ForeignKey(
    #     LocationVO,
    #     related_name="hats",
    #     on_delete=models.CASCADE,
    # )

    def __str__(self):
        return f"{self.id} - {self.fabric}/{self.style_name}/{self.color}"

    