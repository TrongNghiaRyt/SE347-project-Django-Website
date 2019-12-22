from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:eid>', views.test, name='test'),
    path('results/<int:exam_id>/', views.result, name='result'),
]
