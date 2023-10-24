import logging
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException


async def health(request):
    return PlainTextResponse('OK', status_code=200)

async def http_exception(request, e):
    msg, path, code = e.detail, request.scope['path'], e.status_code
    logging.error(f'{msg} ERR_TYPE:{type(e)} ERR_MSG:{str(e)} PATH:{path}')
    return JSONResponse({'result': None, 'error': e.detail}, status_code=code)

async def err404(request, e):
    msg, path = 'Not found', request.scope['path']
    logging.error(f'{msg} ERR_TYPE:{type(e)} PATH:{path}')
    return JSONResponse({'result': None, 'error': msg}, status_code=404)

async def err500(request, e):
    msg, path = 'Server error', request.scope['path']
    logging.error(f'{msg} ERR_TYPE:{type(e)} ERR_MSG:{str(e)} PATH:{path}')
    return JSONResponse({'result': None, 'error': msg}, status_code=500)


exception_handlers = {
    HTTPException: http_exception,
    404: err404,
    500: err500
}
