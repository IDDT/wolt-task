import csv
from typing import Optional


class Database:
    '''This class emulates the database with provided supplimentary file and
    is supposed to be replaced with a proper database adapter for production.
    '''
    def __init__(self, filepath:str):
        self.venue_to_time: dict[str, float] = {}
        with open(filepath, 'rt') as f:
            for record in csv.DictReader(f):
                avg_prep_time = float(record['avg_preparation_time'])
                venue_id = str(record['venue_id'])
                self.venue_to_time[venue_id] = avg_prep_time

    def get_avg_prep_time(self, venue_id:str) -> Optional[float]:
        '''Return average preparation time for venue_id. None if not found.
        '''
        return self.venue_to_time.get(venue_id)
