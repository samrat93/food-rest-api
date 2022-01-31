from django.db import models

# Create your models here.
class Receipe(models.Model):
    """Creating Receipe models"""
    title = models.CharField(max_length=100)
    food_name = models.CharField(max_length=150)
    ingredients = models.CharField(max_length=500)
    cooking_method = models.CharField(max_length=1000)
    def __str__(self):
        """Return title as an object"""
        return self.title
