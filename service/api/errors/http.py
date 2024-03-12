from http import HTTPStatus
from typing import Sequence

from .app import AppError

class NotFoundError(AppError):
    def __init__(
        self,
        status_code: int = HTTPStatus.NOT_FOUND,
        error_key: str = "not_found",
        error_message: str = "Element not found",
        error_loc: Sequence[str] | None = None,
    ):
        super().__init__(status_code, error_key, error_message, error_loc)