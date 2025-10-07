# User.py

from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str
    active: bool


if __name__ == "__main__":

    u = User(1, "Alice", "alice@gmail.com", True)

    print (u)

