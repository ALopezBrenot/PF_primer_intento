from django.urls import path
from AppPosts import views

urlpatterns = [
    path('prueba/', views.prueba, name='prueba')
]