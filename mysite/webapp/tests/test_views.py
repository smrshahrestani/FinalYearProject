# @Author: Seyed Mohammad Reza Shahrestani
# @date: 22/04/2022


from django.test import TestCase
from django.urls import reverse
from django.test import Client
from webapp.views import *
import requests


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()


    def test_playground_response_code_and_template(self):
        response = self.client.get(reverse('playground'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'playground.html')


    def test_stats_response_code_and_template(self):
        response = self.client.get(reverse('stats'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stats.html')


    def test_other_pages_response_302_for_redirect(self):
        response = self.client.get(reverse('redirect'))

        self.assertEqual(response.status_code, 302)


    def test_other_pages_response_404_for_invalid_url(self):
        r = requests.get('http://localhost:8000/not_a_valid_url')
        self.assertEqual(r.status_code, 404)