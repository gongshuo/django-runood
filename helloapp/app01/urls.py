from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello),
    path('add/', views.add_book),
    path('get/', views.get_book),
]