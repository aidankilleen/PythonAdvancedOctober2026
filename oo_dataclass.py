# oo_dataclass.py

from dataclasses import dataclass

@dataclass
class Person:
    id: int
    name: str
    email: str
    active: bool
    _age: int = 21       # property is optional in constructor if default is present

    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError(f"invalid age {value}")
        self._age = value

    def __init__(self, id, name, email, active, age = 21):
        self.id = id
        self.name = name
        self.email = email
        self.active = active
        self.age = age

p = Person(1, "Alice", "alice@gmail.com", True, -99)
print (p)

p.name = "Changed"
print (p)

p1 = Person(1, "Alice", "alice@gmail.com", True)
p2 = Person(1, "Alice", "alice@gmail.com", True)

p1.age = -1



# @dataclass creates properties (no need for __init__)
# @dataclass creates __str__
# @dataclass creates __eq__

if p1 == p2:
    print ("Same")
else:
    print ("different")


