from django.db import models

# Create your models here.
class Book(models.Model):
 bookname = models.CharField(max_length=70)
 authorname = models.CharField(max_length=70)
 
