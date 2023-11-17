from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from base import mods


class PostProcTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        mods.mock_query(self.client)

    def tearDown(self):
        self.client = None

    def test_identity(self):
        data = {
            'type': 'IDENTITY',
            'options': [
                { 'option': 'Option 1', 'number': 1, 'votes': 5 },
                { 'option': 'Option 2', 'number': 2, 'votes': 0 },
                { 'option': 'Option 3', 'number': 3, 'votes': 3 },
                { 'option': 'Option 4', 'number': 4, 'votes': 2 },
                { 'option': 'Option 5', 'number': 5, 'votes': 5 },
                { 'option': 'Option 6', 'number': 6, 'votes': 1 },
            ]
        }

        expected_result = [
            { 'option': 'Option 1', 'number': 1, 'votes': 5, 'postproc': 5 },
            { 'option': 'Option 5', 'number': 5, 'votes': 5, 'postproc': 5 },
            { 'option': 'Option 3', 'number': 3, 'votes': 3, 'postproc': 3 },
            { 'option': 'Option 4', 'number': 4, 'votes': 2, 'postproc': 2 },
            { 'option': 'Option 6', 'number': 6, 'votes': 1, 'postproc': 1 },
            { 'option': 'Option 2', 'number': 2, 'votes': 0, 'postproc': 0 },
        ]

        response = self.client.post('/postproc/', data, format='json')
        self.assertEqual(response.status_code, 200)

        values = response.json()
        self.assertEqual(values, expected_result)

    def test_dhondt_basic(self):
        data = {
            'seats': 3,
            'type': 'DHONDT',
            'options': [
                { 'option': 'Option 1', 'votes': 6 },
                { 'option': 'Option 2', 'votes': 3 },
                { 'option': 'Option 3', 'votes': 1 },
            ]
        }

        expected_result = {'Option 1': 2, 'Option 2': 1, 'Option 3': 0}

        response = self.client.post('/postproc/', data, format='json')
        self.assertEqual(response.status_code, 200)

        values = response.json()
        self.assertEqual(values, expected_result)

    def test_dhondt_performance(self):
        # Genera un conjunto de datos grande para probar el rendimiento
        data = {'seats': 10, 'type': 'DHONDT', 'options': [{'option': str(i), 'votes': 10} for i in range(10000)]}
        
        # Mide el tiempo que tarda en ejecutarse el método dhondt
        import time
        start_time = time.time()
        response = self.client.post('/postproc/', data, format='json')
        end_time = time.time()
    
        # Ajusta el límite de tiempo según sea necesario
        time_limit = 1.0  # en segundos
        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(end_time - start_time, time_limit)





    
