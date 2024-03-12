from fastapi import Request

from service.api.auth import SimpleBearerAuth


class NoAuth(SimpleBearerAuth):
    async def __call__(self, request: Request):
        return True
