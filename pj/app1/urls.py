from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about),
    path('add', views.add),
]
