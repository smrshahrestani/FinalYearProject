from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('playground', views.playground),
    path('playground/query', views.query),
    path('stats', views.stats),
    path('stats/results', views.statsData),
    path('stats/apply', views.apply),
    path('', RedirectView.as_view(url='stats')),
]