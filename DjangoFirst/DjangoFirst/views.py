from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  """ return HttpResponse("Hello, world. Home route") """
  return render(request, 'index.html')

def about(request):
  return HttpResponse("Hello, world. About route")

def contact(request):
  return HttpResponse("Hello, world. Contact route")