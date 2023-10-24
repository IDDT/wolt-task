import logging
import pydantic
from starlette.responses import JSONResponse
from ..types import RequestBody


async def index(request):
    '''Return delivery duration given JSON with following keys
    Request:
        time_received: str
        is_retail: bool
        venue_id: str
    Response:
        result: int | None
        error: None | str
    '''
    #Parse request body.
    body_raw = await request.json()
    try:
        body = RequestBody(**body_raw)
    except pydantic.ValidationError as e:
        msg = 'Request body is missing required keys or cant be parsed'
        logging.error(f'{msg} {body_raw}')
        return JSONResponse({'result': None, 'error': msg}, status_code=400)
    # Get supplimentary data from the database. Empty response if missing.
    database, venue_id = request.app.state.database, body.venue_id
    if (avg_prep_time := database.get_avg_prep_time(venue_id)) is None:
        logging.warning(f'No average time for venue_id: {venue_id}')
        return JSONResponse({'result': None, 'error': None}, status_code=200)
    # Make model input & run inference.
    model_input = body.to_model_input(avg_prep_time)
    result = request.app.state.model(model_input)
    return JSONResponse({'result': result, 'error': None})
