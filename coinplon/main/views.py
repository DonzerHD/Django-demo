from django.shortcuts import render

# Create your views here.

def multiplicated_by_5(num):
    return num * 5

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')