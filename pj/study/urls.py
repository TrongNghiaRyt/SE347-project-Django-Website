from django.urls import path, include
from . import views

urlpatterns = [
    path('question/<slug:kinds>', views.viewQuestion, name='question'),
]