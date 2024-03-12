from typing import Sequence

from .app import AppError


class NotFoundError(AppError):
    def __init__(
        self,
        status_code: int = 404,
        error_key: str = "not_found",
        error_message: str = "Element not found",
        error_loc: Sequence[str] = None,
    ):
        super().__init__(status_code, error_key, error_message, error_loc)
