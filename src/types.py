import datetime
from typing import NamedTuple
from pydantic import BaseModel


class ModelInput(NamedTuple):
    '''A data structure representing model input.
    '''
    is_retail: int
    avg_prep_time: float
    hour_of_day: int

class RequestBody(BaseModel):
    '''A Pydantic model representing the request body.
    '''
    time_received:datetime.datetime
    is_retail:bool
    venue_id:str

    def to_key(self):
        '''Create cache key.
        '''
        return f'{self.time_received.hour}:{self.is_retail}:{self.venue_id}'

    def to_model_input(self, avg_prep_time:float) -> ModelInput:
        '''Create model input.
        '''
        return ModelInput(
            is_retail=int(self.is_retail),
            avg_prep_time=avg_prep_time,
            hour_of_day=self.time_received.hour
        )
