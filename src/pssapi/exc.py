from typing import Optional


class PusherConnectionClosed(Exception):
    """
    Raised when a Pusher connection is closed.
    """
    def __init__(self, message: str, code: Optional[int] = None, error_message: Optional[str] = "") -> None:
        super().__init__(message)

        self.message = message
        self.code = code
        self.error_message = error_message
