from django.db import models

# Create your models here.


class Brand(models.Model):
    name_brand = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo_image', null=True, blank=True)

    def __str__(self):
        return self.name_brand
