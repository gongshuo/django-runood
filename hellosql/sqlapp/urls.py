from django.urls.conf import path,include
from . import  views


app_name = 'sqlapp'

urlpatterns = [
    path('add/', views.add_book),
    path('add2/', views.add_book2),
    path('add3/', views.add_book3),
    path('add4/', views.add_book4),
]
