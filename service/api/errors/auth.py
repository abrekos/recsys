from http import HTTPStatus
from typing import Sequence

from .app import AppError

class AuthError(AppError):
    def __init__(
        self,
        status_code: int = HTTPStatus.FORBIDDEN,
        error_key: str = "invalid_token",
        error_message: str = "Invalid Bearer Token",
        error_loc: Sequence[str] | None = None,
    ):
        super().__init__(status_code, error_key, error_message, error_loc)