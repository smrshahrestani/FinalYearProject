# mysite/webapp/tests/test_urls.py

# @Author: Seyed Mohammad Reza Shahrestani
# @date: 22/04/2022


from django.test import SimpleTestCase
from django.urls import reverse, resolve
from webapp.views import *


# A Test Class for testing the URLs
class TestUrls(SimpleTestCase):
    
    def test_playground_url(self):
        url = reverse('playground')
        self.assertEqual(resolve(url).func, playground)


    def test_playground_query_url(self):
        url = reverse('playground_query')
        self.assertEqual(resolve(url).func, query)


    def test_stats_url(self):
        url = reverse('stats')
        self.assertEqual(resolve(url).func, stats)


    def test_stats_results_url(self):
        url = reverse('stats_results')
        self.assertEqual(resolve(url).func, statsData)


    def test_stats_apply_url(self):
        url = reverse('stats_apply')
        self.assertEqual(resolve(url).func, apply)


    def test_redirect_url_not_equal_to_other_urls(self):
        url = reverse('redirect')
        self.assertNotEqual(resolve(url).func, playground)
        self.assertNotEqual(resolve(url).func, query)
        self.assertNotEqual(resolve(url).func, stats)
        self.assertNotEqual(resolve(url).func, statsData)
        self.assertNotEqual(resolve(url).func, apply)