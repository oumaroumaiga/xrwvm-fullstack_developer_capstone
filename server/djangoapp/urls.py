from django.urls import path
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Path for registration
    path('registration/', views.registration, name='registration'),
    # Path for login
    path('login/', views.login_user, name='login'),
    # Path for logout
    path('logout/', views.logout_request, name='logout'),
    # Path for retrieving car models
    path('get_cars/', views.get_cars, name='get_cars'),
    # Path for retrieving dealerships
    path('get_dealers/', views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>/', views.get_dealerships, name='get_dealers_by_state'),
    # Path for retrieving dealership details
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    # Path for retrieving dealer reviews
    path('reviews/dealer/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),
    # Path for adding a review
    path('add_review/', views.add_review, name='add_review'),
] 
