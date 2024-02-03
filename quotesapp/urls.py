from django.urls import path
from . import views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('add_quote/', views.add_quote, name='quote'),
    path('tag/', views.tag, name='tag'),
]