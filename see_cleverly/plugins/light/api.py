from fastapi import APIRouter

light_router = APIRouter(prefix="/light")


@light_router.get("/overview/{id}", tags=["light"])
async def light_overview(id: int):
    return {"customer_id": id, "indoor": 7, "outdoor": 3}
