#1. class defination is one time process
class MyClass():
    #1 Property=Variable
    # We can use multiple properties
    name="Vishal"
    surname="Mahawar"
    address="Neemuch"
    age=15

    #3. Method = Function
    # We can use multple method
    def getMyAge(self):# camleCase
        print(self.age)
        
        self.getMyName()
        pass
    
    def getMyName(self):# camleCase
        #2. calling
        print(self.name)
        pass
    pass
#2. create class object in many time process
ceo=MyClass()
print(ceo.getMyAge())