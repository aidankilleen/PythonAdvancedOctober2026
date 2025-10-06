# Person.py

from functools import total_ordering


@total_ordering
class Person():
    def __init__(self, id:int, name:str, email:str, active:bool):
        self.id = id
        self.name = name
        self.email = email
        self.active = active
        pass

    def __str__(self):
        return f"id={self.id}\nname={self.name}\nemail={self.email}\n{self.active}"

    def __repr__(self):
        return f"(id={self.id} name={self.name} email={self.email} {self.active})"

    def __eq__(self, other):
        if self.id == other.id and self.name == other.name and self.email == other.email and self.active == other.active:
            return True
        else: 
            return False
    def __lt__(self, other):
        print (f"comparing {self.name} to {other.name}")
        return self.name < other.name
