# timer_decorator.py

import time

# decorators added 3.6
# we may no create many decorators but they are used a lot in some of the libraries we will encounter



def timing(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print (f"function took {end_time - start_time:.5f}s")
        pass

    return wrapper

@timing
def do_something():
    print ("starting")
    time.sleep(5)
    print ("end")

do_something()

@timing
def do_something_else():
    t = 0
    for i in range(100000000):
        t+=i
    print (f"Total is {t}") 

do_something_else()