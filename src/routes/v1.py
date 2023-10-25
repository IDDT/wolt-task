import logging
import pydantic
from starlette.responses import JSONResponse
from ..config import REDIS_EXPIRE_S
from ..types import RequestBody


async def index(request):
    '''Handle incoming JSON data to predict delivery duration.
    Request:
        JSON with the following keys:
            - time_received (str): The timestamp of the order.
            - is_retail (bool): Whether the order is retail.
            - venue_id (str): Identifier of the venue.
    Response:
        JSON response with the following keys:
            - result (int | None): Predicted delivery duration in minutes or None if not available.
            - error (None | str): An error message or None if no errors occurred.
    '''
    # Parse request body.
    body_raw = await request.json()
    try:
        body = RequestBody(**body_raw)
    except pydantic.ValidationError as e:
        msg = 'Request body is missing required keys or cant be parsed'
        logging.error(f'{msg} {body_raw}')
        return JSONResponse({'result': None, 'error': msg}, status_code=400)

    # Check for cached value.
    cache, cache_key = request.app.state.cache, body.to_key()
    if (result := await cache.get(cache_key)) is None:

        # Get supplimentary data from the database. Empty response if missing.
        database, venue_id = request.app.state.database, body.venue_id
        if (avg_prep_time := database.get_avg_prep_time(venue_id)) is None:
            logging.warning(f'No average time for venue_id: {venue_id}')
            return JSONResponse({'result': None, 'error': None}, status_code=200)

        # Make model input & run inference.
        model_input = body.to_model_input(avg_prep_time)
        result = request.app.state.model(model_input)

        # Cache the result.
        await cache.setex(cache_key, REDIS_EXPIRE_S, result)

    return JSONResponse({'result': result, 'error': None})
