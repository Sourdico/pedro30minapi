# This imports Django REST Framework’s serializer module.
# It's used to convert model instances (like User) into JSON format and vice versa.
from rest_framework import serializers

# This imports your custom User model, which represents the table in the database.
from .models import User


# This is your own custom serializer class.
# It tells Django REST Framework how to convert User objects <-> JSON.
class UserSerializer(serializers.ModelSerializer):

    # Meta class is Django convention for providing metadata about the serializer.
    class Meta:
        # Tells the serializer which model it is linked to.
        model = User  # <-- This is your custom model

        # Tells the serializer to include all fields from the User model: id (auto), name, and age.
        fields = '__all__'  # <-- This means include every field from the model
