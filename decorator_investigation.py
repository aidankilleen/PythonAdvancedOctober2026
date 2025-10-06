# decorator_investigation.py

#def greet():
#    return ("Hello")

def loud(func):
    def wrapper():
        return func().upper()
    
    return wrapper

#shout = loud(greet)
@loud
def greet():
    return "hello"

print(greet())



# decorator that takes a parameter
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hi(name):
    print (f"Hi {name}")

hi("Aidan")

@repeat(5)
def hello(name):
    print (f"hello {name}")

hello("Alice")








#@loud
#def create_message(greeting, name):
#    return greeting + " " + name


#print (create_message("Hello", "Aidan"))

