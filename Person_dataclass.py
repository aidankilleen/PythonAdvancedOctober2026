# Person_dataclass.py

from dataclasses import dataclass


@dataclass(order=True)
class Person:
    id: int
    name: str
    email: str
    active: bool
    _age: int = 21       # property is optional in constructor if default is present

