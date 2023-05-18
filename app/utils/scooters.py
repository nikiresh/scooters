import typing as tp

from app.context import AppContext
from app import dto
from app import storage
from app.utils import geocode

async def _enrich_address(scooters: tp.List[dto.Scooter], client: geocode.GeocoderClient) -> None:
    for scooter in scooters:
        scooter.address = client.get_address(scooter.location)


async def get_scooter(context: AppContext) -> tp.List[dto.Scooter]:
    scooters = [
        dto.Scooter.from_model(scooter)
        for scooter in await storage.get_scooters(context)
    ]

    await _enrich_address(scooters, context.geocoder)

    return scooters