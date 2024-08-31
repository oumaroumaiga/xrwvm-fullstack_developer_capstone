from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import logging
import json
from datetime import datetime

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# Create a `login_request` view to handle sign-in requests
@csrf_exempt
def login_user(request):
    # Get username and password from request.body
    data = json.loads(request.body)
    username = data.get('userName')
    password = data.get('password')
    
    # Try to authenticate provided credentials
    user = authenticate(username=username, password=password)
    response_data = {"userName": username}
    
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        response_data = {"userName": username, "status": "Authenticated"}
    
    return JsonResponse(response_data)

# Create a `logout_request` view to handle sign-out requests
@csrf_exempt
def logout_request(request):
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        response_data = {"userName": username}
    else:
        response_data = {"error": "No user is logged in"}
    
    return JsonResponse(response_data)

# Create a `registration` view to handle sign-up requests
# @csrf_exempt
# def registration(request):
#     ...

# Update the `get_dealerships` view to render the index page with a list of dealerships
# def get_dealerships(request):
#     ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request, dealer_id):
#     ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
#     ...

# Create a `add_review` view to submit a review
# def add_review(request):
#     ...
