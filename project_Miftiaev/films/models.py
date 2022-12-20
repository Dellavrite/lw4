from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('name', 'name', max_length=50)
    

class Film(models.Model):
    name = models.CharField('name', 'name', max_length=255)
    categorys = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_post = models.DateField('date_post', 'date_post')
    actors = models.CharField('actors', 'actors', max_length=255)
    date_view = models.DateField('date_view', 'date_view')
    
