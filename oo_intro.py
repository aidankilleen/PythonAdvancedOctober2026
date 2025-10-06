# oo_intro.py

# explore a little about object oriented programming in python
# type hints
class Person():
    def __init__(self, id:int, name:str, email:str, active:bool):
        self.id = id
        self.name = name
        self.email = email
        self.active = active
        pass

    def display(self):
        print (self)

    def __str__(self):
        return f"id={self.id}\nname={self.name}\nemail={self.email}\n{self.active}"

    def __repr__(self):
        return f"(id={self.id} name={self.name} email={self.email} {self.active})"
        #return str(self)

    def __eq__(self, other):
        if self.id == other.id and self.name == other.name and self.email == other.email and self.active == other.active:
            return True
        else: 
            return False
        
    #def __lt__(self, other):
    #    print (f"comparing {self.id} to {other.id}")
    #    return self.id < other.id
    def __lt__(self, other):
        print (f"comparing {self.name} to {other.name}")
        return self.name < other.name

if __name__ == "__main__":
    # p6 = Person("ABC123", "Aidan", "aidan@gmail.com", 1234)
    p7 = Person(1, "Alice", "alice@gmail.com", True)
    p8 = Person(1, "Alice", "alice@gmail.com", True)

    if p7 == p8:
        print ("same")
    else:
        print ("different")


    print ("=" * 30)

    r = list(range(10))

    def do_something(p:Person) -> None:
        print (f"do something with {p.name}")
        # return 123


    do_something(p7)


    # D.R.Y.
    # don't repeat yourself!!!
    # prime directive

    p = Person(1, "Aidan", "aidan@gmail.com", True)
    p.display()

    print (p)

    print ("hello")






    p.active = False
    p.display()


    # p is an instance of the Person class
    print (p.name)
    #p2 = Person(2, "Alice", "alice@gmail.com", 1234)
    #print (p2.name)
    #p3 = Person()
    #p3.id = 1
    #p3.name = "Bob"
    #p3.email = "bob@gmail.com" 
    #p3.active = True
