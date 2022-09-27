from django.db import models
from brands.models import Brand


# Create your models here.
class Model(models.Model):
    name = models.CharField(max_length=100)
    engine = models.CharField(max_length=50)
    hp = models.IntegerField(null=True)
    nm = models.IntegerField(null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False)
    model_photo = models.ImageField(upload_to='model_photo', null=True, blank=True)

    def __str__(self):
        return self.name


class Series(models.Model):
    series_name = models.CharField(max_length=50)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=False)
    series_photo = models.ImageField(upload_to='series_photo', null=True, blank=True)

    def __str__(self):
        return self.series_name
