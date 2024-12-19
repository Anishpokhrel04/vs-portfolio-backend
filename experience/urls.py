from django.urls import path
from . import views

urlpatterns = [
    path('experiences/', views.experience_list, name='experience-list'),
    path('experiences/<int:pk>/', views.experience_detail, name='experience-detail'),
]
