from django.db import models
from users.models import CustomUser

# Create your models here.


class Book(models.Model):           # Table Definition
    # Attributes
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    price = models.IntegerField()
    pages = models.IntegerField()
    cover = models.ImageField(upload_to='images', blank=True, null=True)
    pdf = models.FileField(upload_to='pdf', blank=True, null=True)
    details = models.CharField(max_length=30)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title



