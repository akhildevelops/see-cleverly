from fastapi import APIRouter
from .light import light_router

plugin_router = APIRouter(prefix="/plugin")

for router in [light_router]:
    plugin_router.include_router(router)