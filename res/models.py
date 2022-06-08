from django.db import models
from accounts.models import AppUser
# Create your models here.

class Res(models.Model):
    name =models.CharField(max_length=20,unique=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    phone=models.CharField(max_length=15,null=True,blank=True)
    category = models.CharField(max_length=20,null=True,blank=True)
'''
    def _str__(self):
        return self.name
'''
class Review(models.Model):
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='author_review',db_column='author')
    res = models.ForeignKey(Res,on_delete=models.CASCADE, related_name='res_review',db_column='res')
    score = models.FloatField(null=False,blank=False)
    comment = models.TextField(null=True,blank=True)
    create_date = models.DateTimeField()
    class Meta:
        constraints = [models.UniqueConstraint(fields=['author','res'] ,name='unique_author_res_combination'),]

class reserve(models.Model):
    name = models.CharField(max_length=20, unique=False)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)