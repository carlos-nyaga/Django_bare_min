from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views
app_name='core'

urlpatterns = [

    # The index page
    path('', views.index, name='index'),

]
