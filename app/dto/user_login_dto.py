from dataclasses import dataclass


@dataclass
class UserLoginDTO:
    username: str
    password: str
