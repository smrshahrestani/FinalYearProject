from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('query', views.query),
    path('stats', views.stats)
]