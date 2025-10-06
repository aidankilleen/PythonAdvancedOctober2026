# CountyList.py

class CountyList():

    def __init__(self):
        self.counties = []

    def add(self, county):
        self.counties.append(county)

    def __len__(self):
        return len(self.counties)
    
    def __getitem__(self, i):
        return self.counties[i]
    
    def __iter__(self):
        return iter(self.counties)

cl = CountyList()

cl.add("Dublin")
cl.add("Cork")
cl.add("Limerick")
cl.add("Clare")
cl.add("Kerry")
cl.add("Waterford")

# can I access an idividual item
print (cl[4])

# can I slice my custom class
for county in cl[2:4]:
    print (county)

print ("=" * 30)
# can I iterate through my custom class?
for county in cl:
    print (county)

print ("=" * 30)
for county in cl[::-1]:
    print (county)


#print (len(cl))

#cl.add("Galway")
#print (len(cl))

#cl.add("Clare")
#print (len(cl))







