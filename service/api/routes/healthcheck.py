from fastapi import APIRouter, Depends

from service.api.auth import bearer_auth
from service.api.types.health import HealthStatus

router = APIRouter()


@router.get(
    "",
    dependencies=[Depends(bearer_auth)],
    responses={200: {"model": HealthStatus}},
)
async def health() -> HealthStatus:
    return HealthStatus(status="ok")
