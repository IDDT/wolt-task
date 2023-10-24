from starlette.applications import Starlette
from starlette.routing import Route
from .routes import system, v1
from .config import FILEPATHS
from .database import Database
from .model import Model


app = Starlette(
    debug=False,
    routes=[
        Route('/', v1.index, methods=['POST']),
        Route('/health', system.health, methods=['GET'])
    ],
    exception_handlers=system.exception_handlers
)


app.state.model = Model(FILEPATHS['model_artifact'])
app.state.database = Database(FILEPATHS['venue_preparation'])
