#1. class defination is one time process
class MyClass():
    #1 member
    #2 member
    #3 method defination is one time process
    def myFunction(self):
        print(f'GoodMorning Vishal')
        pass

#2. create class object is many time process
ceo1=MyClass()

#3.2 method calling/inovking is many time process
ceo1.myFunction() 
