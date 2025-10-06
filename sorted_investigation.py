# sorted_investigation.py

from operator import attrgetter
from Person_dataclass import Person

numbers = [1, 4, 2, 6, 3, 8, 9, 10, 4]

people = [
  Person(99, "Zoe", "zoe@gmail.com", True), 
  Person(27, "Yvonne", "yvonne@gmail.com", False), 
  Person(83, "Alice", "alice@gmail.com", False), 
  Person(42, "Marie", "marie@gmail.com", True), 
  Person(12, "Jean", "jean@gmail.com", False), 
   ]
sorted_numbers = sorted(numbers)

print (numbers)
print (sorted_numbers)


sorted_people = sorted(people)
print (people)
print (sorted_people)

print (people[0])
print (people[1])

if people[1] > people[0]:

    print ("greater")
else:
    print ("not greater")

#people[0]


people.sort(key=attrgetter("name"))

print (people)









