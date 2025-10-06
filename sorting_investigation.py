# sorting_investigation.py

numbers = [1, 4, 2, 6, 3, 8, 9, 10, 4]
print (numbers)

numbers.sort()
print (numbers)


from operator import attrgetter
from oo_intro import Person

people = [
  Person(1, "Zoe", "zoe@gmail.com", True), 
  Person(2, "Yvonne", "yvonne@gmail.com", False), 
  Person(3, "Alice", "alice@gmail.com", False), 
  Person(4, "Marie", "marie@gmail.com", True)
   ]
print (people)

#people.sort(key=lambda p: p.name)

people.sort(key=attrgetter("name"), reverse=True)

print (people)


#print (people[0])


#print (str(people[0])) # explictly call __str__

#print (repr(people[0])) # 

