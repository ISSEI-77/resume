from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('resume1/', views.resume1, name="resume1"),
    path('resume2/', views.resume2, name="resume2"),
]
