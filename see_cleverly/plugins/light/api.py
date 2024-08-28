from fastapi import APIRouter, Depends
from typing import Annotated
from ...database import get_db
from . import LightRepository
from psycopg_pool.pool_async import AsyncConnectionPool

light_router = APIRouter(prefix="/light")


@light_router.get("/overview/{id}", tags=["light"])
async def light_overview(
    id: int, pool: Annotated[AsyncConnectionPool, Depends(get_db)]
):
    lr = LightRepository(pool)
