# builder_investigation.py


class Person():
    def __init__(self, id, name, email="", active=False, county="", country=""):
        self._id = id
        self._name = name
        self._email = email
        self._active = active
        self._county = county
        self._country = country

    def __str__(self):
        return f"Person Object: {self._id} {self._name} {self._email}"
    def id(self, id):
        self.id = id

    def name(self, name):
        self.name = name

class PersonBuilder():
    def __init__(self):
        self._id = 0
        self._name = ""
        self._email = ""
        self._active = False
        self._count = ""
        self._country = ""

    def id(self, id):
        self._id = id
        return self

    def name(self, name):
        self._name = name
        return self
    
    def email(self, email):
        self._email = email
        return self

    def build(self):
        if self._id == 0:
            raise ValueError("Can't create Person with no id or id=0")
        return Person(self._id, self._name, self._email)
    pass

p = (
    PersonBuilder()
     .email("Alice@gmail.com")
     .id(1)
     .name("Alice")
     .build()
)

print (p)

