from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptname=models.CharField(max_length=100)
    loc=models.charfield(max_length=100)