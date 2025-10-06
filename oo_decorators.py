# oo_decorators.py


class Person():
    def __init__(self, name, age=21) -> None:
        self._name = name
        self._age = age
        pass
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value) -> None:
        if value >= 0 and value <= 120:
            self._age = value
        else:
            raise ValueError(f"Invalid age {value}")
    
    def __str__(self):
        return f"{self.name} {self.age}"

p = Person("Alice")

# encapsulation
# protecting the values of the properties(state) of my object from invalid values
p.age = -1
print(p)

p.name = "Changed Name"
print (p)

