# Import Django REST Framework decorator to declare which HTTP methods the view accepts
from rest_framework.decorators import api_view

# Import Django REST Framework's Response object to return API responses in JSON format
from rest_framework.response import Response

# Import standard HTTP status codes to send correct responses like 201 Created, 404 Not Found, etc.
from rest_framework import status

# Import your User model (your database table)
from .models import User

# Import your UserSerializer to convert model instances to/from JSON
from .serializer import UserSerializer


# This is your custom view function to handle GET requests for the list of users
@api_view(['GET'])  # Decorator specifies this view only accepts GET requests
def get_user(request):
    # Fetch all User objects from the database (Django ORM query)
    users = User.objects.all()
    
    # Serialize many=True because we have a queryset (multiple users)
    serializer = UserSerializer(users, many=True)
    
    # Return serialized data as JSON response (Django REST Framework Response)
    return Response(serializer.data)  # <-- This returns the list of users as JSON


# This is your custom view function to handle POST requests to create a new user
@api_view(['POST'])  # Decorator limits this to POST method only
def create_user(request):
    # Pass incoming JSON data (request.data) into the serializer to validate and deserialize
    serializer = UserSerializer(data=request.data)
    
    # Check if the data is valid according to the serializer/model rules
    if serializer.is_valid():
        # Save the new User instance in the database
        serializer.save()
        
        # Return the serialized data with HTTP 201 Created status
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # If data invalid, return errors with HTTP 400 Bad Request status
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This is your custom view to handle GET, PUT, DELETE for a single user identified by primary key (pk)
@api_view(['GET', 'PUT', 'DELETE'])  # Accept these HTTP methods
def user_detail(request, pk):
    try:
        # Try fetching the user object by primary key from DB
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        # If user not found, return HTTP 404 Not Found
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Handle GET request: return user data as JSON
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    # Handle PUT request: update user data with new info from request.data
    elif request.method == 'PUT':
        # Pass existing user instance + new data to serializer for validation and update
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save updated user
            return Response(serializer.data)
        # If invalid data, return errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Handle DELETE request: remove user from database
    elif request.method == 'DELETE':
        user.delete()
        # Return HTTP 204 No Content on successful deletion
        return Response(status=status.HTTP_204_NO_CONTENT)
