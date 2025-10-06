# named_tuple_investigation.py
from collections import namedtuple

# use a named tuple if you just need properties
# and don't need any methods

Person = namedtuple("Person", ["id", "name", "email", "active"])


p = Person(1, "Aidan", "aidan@gmail.com", True)

print (p.name)
print (p)

#p.name = "Changed"




