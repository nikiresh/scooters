from aiohttp import web

from app.context import AppContext
from app.utils import scooters as scooters_utils
from app import dto


async def handle(request: web.Request, context: AppContext) -> web.Response:
    scooters = await scooters_utils.get_scooter(context)
    return web.json_response({'items': [
        to_responce(scooter) for scooter in scooters
    ]})

def to_responce(scooter: dto.Scooter) -> dict:
    return {
        'id': scooter.id,
        'location': [scooter.location.lat, scooter.location.lon]
    }