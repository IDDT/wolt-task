import unittest
from src.config import FILEPATHS
from src.database import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = Database(FILEPATHS['venue_preparation'])

    def test_get_avg_prep_time_existing_venue(self):
        avg_prep_time = self.database.get_avg_prep_time('8a61b70')
        self.assertEqual(avg_prep_time, 11.700400677533139)

    def test_get_avg_prep_time_nonexistent_venue(self):
        avg_prep_time = self.database.get_avg_prep_time('nonexistent_venue')
        self.assertIsNone(avg_prep_time)
