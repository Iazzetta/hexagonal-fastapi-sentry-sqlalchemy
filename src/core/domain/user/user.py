from dataclasses import dataclass

@dataclass
class User:
    name: str = None
    email: str = None
    password: str = None