# mysite/webapp/urls.py

# @Author: Seyed Mohammad Reza Shahrestani
# @date: 22/04/2022


from django.urls import path
from . import views
from django.views.generic.base import RedirectView


# URL Patterns
# Sends the URLs to their corresponding function
# Set name to the paths for testing
# Redirects the home page to the stats page
urlpatterns = [
    path('playground', views.playground, name='playground'),
    path('playground/query', views.query, name='playground_query'),
    path('stats', views.stats, name='stats'),
    path('stats/results', views.statsData, name='stats_results'),
    path('stats/apply', views.apply, name='stats_apply'),
    path('', RedirectView.as_view(url='stats'), name='redirect'),
]