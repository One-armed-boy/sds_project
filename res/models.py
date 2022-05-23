from django.db import models
from account.models import User
# Create your models here.

class Res(models.Model):
    name =models.CharField(max_length=20,null=False,blank=False)
    address=models.CharField(max_length=50,null=True,blank=True)
    phone=models.CharField(max_length=15,null=True,blank=True)
'''
    def _str__(self):
        return self.name
'''
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_review')
    res = models.ForeignKey(Res,on_delete=models.CASCADE, related_name='res_review')
    is_pred=models.BooleanField(default=True,null=False,blank=False)
    score = models.FloatField(null=False,blank=False)
    comment = models.TextField(null=True,blank=True)
    create_date = models.DateTimeField()