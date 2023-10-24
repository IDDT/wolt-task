import unittest
import datetime
from src.types import ModelInput, RequestBody


class TestTypes(unittest.TestCase):
    def test_model_input_creation(self):
        model_input = ModelInput(
            is_retail=1,
            avg_prep_time=20.5,
            hour_of_day=15
        )
        self.assertEqual(model_input.is_retail, 1)
        self.assertEqual(model_input.avg_prep_time, 20.5)
        self.assertEqual(model_input.hour_of_day, 15)

    def test_request_body_to_model_input(self):
        request_body = RequestBody(
            time_received=datetime.datetime(2023, 10, 24, 15, 30),
            is_retail=True,
            venue_id='123'
        )
        avg_prep_time = 18.5
        model_input = request_body.to_model_input(avg_prep_time)
        self.assertEqual(model_input.is_retail, 1)
        self.assertEqual(model_input.avg_prep_time, 18.5)
        self.assertEqual(model_input.hour_of_day, 15)

    def test_request_body_invalid_is_retail(self):
        with self.assertRaises(ValueError):
            RequestBody(
                time_received=datetime.datetime(2023, 10, 24, 15, 30),
                is_retail='invalid',
                venue_id='123'
            )
