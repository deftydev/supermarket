from django.db import models

from django.contrib.auth.models import User

class Product(models.Model):

    contact     =models.CharField(max_length=100)
    number      =models.IntegerField()
    title       =models.CharField(max_length=40)
    description =models.CharField(max_length=40)
    image       =models.ImageField(upload_to='images/',blank=True)
    votes_total =models.IntegerField(default=1 )



    def __str__(self):
        return self.title

    class Meta:
        ordering=['-id']
