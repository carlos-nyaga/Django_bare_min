from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

def index(request):
    return render(request, 'core/base.html')
