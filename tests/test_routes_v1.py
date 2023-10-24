import unittest
from starlette.testclient import TestClient
from src import app


class TestRoutesV1(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_index_route_valid_input(self):
        response = self.client.post('/', json={
            'time_received': '2023-10-24T12:00:00',
            'is_retail': True,
            'venue_id': '12345'
        })
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn('result', response_data)
        self.assertIn('error', response_data)
        self.assertIsNone(response_data['error'])

    def test_index_route_missing_keys(self):
        invalid_request_body = {'is_retail': True}
        response = self.client.post('/', json=invalid_request_body)
        self.assertEqual(response.status_code, 400)
        response_data = response.json()
        self.assertIn('error', response_data)
        self.assertIsNotNone(response_data['error'])

    def test_index_route_missing_average_time(self):
        response = self.client.post('/', json={
            'time_received': '2023-10-24T12:00:00',
            'is_retail': True,
            'venue_id': 'non_existent_venue'
        })
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIsNone(response_data['result'])
