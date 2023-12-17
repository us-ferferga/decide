from django.test import TestCase
from base.tests import BaseTestCase


# Create your tests here.

class BoothTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
    def tearDown(self):
        super().tearDown()
    def testBoothNotFound(self):
        # Se va a probar con el numero 10000 pues en las condiciones actuales en las que nos encontramos no parece posible que se genren 10000 votaciones diferentes
        response = self.client.get('/booth/old/10000/')
        self.assertEqual(response.status_code, 404)
    
    def testBoothRedirection(self):
        # Se va a probar con el numero 10000 pues en las condiciones actuales en las que nos encontramos no parece posible que se genren 10000 votaciones diferentes
        response = self.client.get('/booth/old/10000')
        self.assertEqual(response.status_code, 301)

    def testBoothPing(self):
        response = self.client.get('/booth/api', format='json')
        self.assertEqual(response.status_code, 200)

    def testApiNotFound(self):
        response = self.client.get('/booth/api/10000', format='json')
        self.assertEqual(response.status_code, 404)
