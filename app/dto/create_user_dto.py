from dataclasses import dataclass
from typing import Optional


@dataclass
class UserDTO:
    fullname: Optional[str]
    username: Optional[str]
    password: Optional[str]
    scopes: Optional[list]
    is_admin: bool
