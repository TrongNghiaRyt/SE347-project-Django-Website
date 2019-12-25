from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:eid>', views.test, name='test'),
    path('results/<slug:exam_id>/', views.result, name='result'),
]
