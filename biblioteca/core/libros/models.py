from django.db import models

# Create your models here.
class libreria(models.Model):
    id = models.AutoField(primary_key= True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    