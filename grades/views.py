from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html = "Hello, World! You're at the index of grades."
    return HttpResponse(html)
