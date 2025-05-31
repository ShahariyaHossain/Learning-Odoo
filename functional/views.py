from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    """
    Render the home page of the Functional app.
    """
    return HttpResponse("Hello, welcome to the functional app!")