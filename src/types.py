import datetime
from typing import NamedTuple
from pydantic import BaseModel


class ModelInput(NamedTuple):
    is_retail: int
    avg_prep_time: float
    hour_of_day: int


class RequestBody(BaseModel):
    time_received:datetime.datetime
    is_retail:bool
    venue_id:str

    def to_model_input(self, avg_prep_time:float) -> ModelInput:
        return ModelInput(
            is_retail=int(self.is_retail),
            avg_prep_time=avg_prep_time,
            hour_of_day=self.time_received.hour
        )
