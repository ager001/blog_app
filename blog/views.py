from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return HttpResponse("<h1>Welcome to the Blog Home Page!</h1>")

def about(request):
    return HttpResponse("<h1>About the Blog</h1><p>This is a simple blog application built with Django.</p>")
