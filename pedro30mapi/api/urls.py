# Import Django's function to define URL patterns
from django.urls import path

# Import your custom view functions from views.py
from .views import get_user, create_user, user_detail  # <-- Added user_detail import for the third URL

# List of URL routes your app responds to
urlpatterns = [
    # URL: /user/       --> Calls your get_user view (GET request)
    path('user/', get_user, name='get_user'),

    # URL: /user/create/ --> Calls your create_user view (POST request)
    path('user/create/', create_user, name='create_user'),

    # URL: /user/<int:pk> --> Calls your user_detail view (GET, PUT, DELETE request for specific user by pk)
    path('user/<int:pk>/', user_detail, name='user_detail'),  # Fixed: should call user_detail not create_user
]
