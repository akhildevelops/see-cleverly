from fastapi import APIRouter
from ..plugins import plugin_router

api_router = APIRouter(prefix="/api")
api_router.include_router(plugin_router)
