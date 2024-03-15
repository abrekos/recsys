from fastapi import APIRouter, Depends, Request

from service.api.auth import bearer_auth
from service.api.errors.http import NotFoundError
from service.api.types.error import Error
from service.api.types.recommendations import RecoResponse
from service.log import app_logger

router = APIRouter()


@router.get(
    path="/{model_name}/{user_id}",
    dependencies=[Depends(bearer_auth)],
    responses={
        200: {"model": RecoResponse},
        401: {
            "model": Error,
            "description": "Authentication error",
        },
        404: {
            "model": Error,
            "description": "Not Found Error",
        },
    },
)
async def get_reco(request: Request, model_name: str, user_id: int) -> RecoResponse:
    app_logger.info(f"Request for model: {model_name}, user_id: {user_id}")
    models = request.app.state.models

    if model_name not in models.keys():
        raise NotFoundError(error_message="Model not found")

    if user_id > 10**9:
        raise NotFoundError(error_message="User not found")

    model = models[model_name]

    k_recs = request.app.state.k_recs
    reco = model.get_reco(user_id=user_id, num_reco=k_recs)
    return RecoResponse(user_id=user_id, items=reco)
