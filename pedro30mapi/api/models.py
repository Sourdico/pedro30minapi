# This imports Django's built-in tools for creating models (which are basically database tables).
from django.db import models

# This is your own custom model class named "User".
# It inherits from Django's built-in 'models.Model', which means Django will treat this as a database table.
class User(models.Model):
    
    # This defines a column named "age" in the "User" table.
    # IntegerField is a Django-provided field type for storing whole numbers.
    age = models.IntegerField()
    
    # This defines a column named "name" in the "User" table.
    # CharField is a Django-provided field type for storing short text data.
    # max_length=100 means the name can't be longer than 100 characters.
    name = models.CharField(max_length=100)

    # This is your own function that tells Django how to represent the object as a string.
    # When you print a User object, or see it in Django Admin, it will display the user's name.
    def __str__(self):
        return self.name
