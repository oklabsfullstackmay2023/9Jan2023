#1. class defination is one time process
class MyClass():
    #1 Property=Variable
    name="Vishal"
    surname="Mahawar"
    age=15
    address="Neemuch"

    #3 Method=Function
    #Function Defination is one time process
    def getMyAddress(self):#camleCase
        print(self.name)

        self.getMyName()
        pass 

    def getMyName(self):
        #calling
        print(self.address)
        pass

#2. create class object in many time process
ceo1=MyClass()
print(ceo1.name)# i can access property from ceo
print(ceo1.getMyAddress())# i can access method from ceo