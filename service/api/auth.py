from os import getenv

from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from service.api.errors.auth import AuthError


class SimpleBearerAuth(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    def _validate_token(self, token: str) -> bool:
        return token == getenv("BEARER_KEY")

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise AuthError(error_message="Invalid authentication scheme")
            if not self._validate_token(credentials.credentials):
                raise AuthError(error_message="Invalid token or expired token")
            return credentials.credentials

        raise AuthError(error_message="Invalid authorization code")


bearer_auth = SimpleBearerAuth()