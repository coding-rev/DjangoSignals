from django.urls import path   
from .import views

app_name = 'lesson'

urlpatterns = [
    path('', views.Index)
]
