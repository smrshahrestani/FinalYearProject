from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('playground', views.playground, name='playground'),
    path('playground/query', views.query, name='playground_query'),
    path('stats', views.stats, name='stats'),
    path('stats/results', views.statsData, name='stats_results'),
    path('stats/apply', views.apply, name='stats_apply'),
    path('', RedirectView.as_view(url='stats'), name='redirect'),
]