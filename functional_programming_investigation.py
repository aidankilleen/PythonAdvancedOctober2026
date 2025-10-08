# functional_programming_investigation.py

# in python functions are "first class objects"

i = 10
s = "hello"
f = print

# you can assign a function to a variable
f("hello")


def wrapper(f):
    print ("before")
    f()
    print ("after")

def do_something():
    print ("doing something")


wrapper(do_something)

def add(a, b):
    return a+b 

def mul(a, b):
    return a*b

strategies = {
    "add": add, 
    "mul": mul
}

print (strategies["add"](10, 20))
print (strategies["mul"](10, 20))

# lambda defines a function
# anonymous - no name
# before : are the parameters
# after : is the code
# NB: lambda can only have a single line
sub = lambda a,b: a-b

print (sub(10, 5))

strategies = {
    "add": lambda a,b : a+b, 
    "mul": lambda a,b : a*b,
    "sub": lambda a,b : a-b,
    "div": lambda a,b : a/b
}

print (strategies['div'](100, 10))


numbers = [1,2,3,4,5]

def double(x):
    return x * 2

# doubled_numbers = list(map(double, numbers))
doubled_numbers = list(map(lambda x:x*2, numbers))

print (numbers)
print (doubled_numbers)

# filter a list
numbers = range(1, 11)

even_numbers = list(filter(lambda x:x%2==0, numbers))

print (list(numbers))
print (even_numbers)

# lambda are not used as often in python as in other languages
# because list comprehensions are available

even_numbers = [number for number in numbers if number % 2 == 0]
print (even_numbers)

from operator import attrgetter
from User import User

users = [
    User(91, "zalice", "alice@gmail.com", True), 
    User(22, "bob", "bob@gmail.com", True), 
    User(53, "carol", "carol@gmail.com", False), 
    User(4, "adan", "dan@gmail.com", False), 
    ]

active_users = list(filter(lambda u:u.active, users))

print (active_users)

def myattrgetter(u):
    return u.name

#users.sort(key=lambda u: u.id)
users.sort(key=myattrgetter)

print (users)



#sorted()

def sort_by_last_name(name):
    pieces = name.split(" ")
    return pieces[-1]

names = ["dan thompson", "john barry murphy", "bob murphy", "carol keane", "alice zapone"]

#names.sort(key = sort_by_last_name)

#sort_by_last_name = lambda name: name.split(" ")[-1]
#names.sort(key = sort_by_last_name)


names.sort(key = lambda name: name.split(" "[-1]))
print (names)

max_user = max(users, key=lambda u: u.name)
print (max_user)
















































