from pony.orm import db_session as db_session
from typing import Any, Optional

class Pony:
    app: Any = ...
    def __init__(self, app: Optional[Any] = ...) -> None: ...
    def init_app(self, app: Any) -> None: ...
