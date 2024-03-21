
##1 Tasks
## Write the code for the below tasks using function
##1.) dl ("shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}
##a.) Find the min ans max priced product
##b.) Find the product starts with 's' and 'S'

##2.) Find then 67, is strong number or not
##
##3.) 11 [1,2,3,4,5,6]
##n=2> [5, 6, 1,2,3,4]
##n=3--> [4,5,6, 1,2,3]

## ! method riding
## * Polymorphism in classes using inheritance

## ? Eg:1
##class bank :
##    def ratio(self):
##        print(" All banks has repo rate")
##
##class SBI(bank):
##    def ratio(self):
##        print("SBI rate is 9%")
##
##class IOB(bank):
##    def ratio(self):
##        print("IOB rate is 7.5%")
##
##i = IOB()
##i.ratio()
##
##s= SBI()
##s.ratio()

## ? Eg:2
##class USA:
##    def language(self):
##        print("ENGLISH")
##
##    def captail(self):
##        print("Washington DC")
##
##class India(USA):
##    def language(self):
##        print("sansrit")
##
##    def captail(self):
##        print("New delhi")
##
##I = India()
##I.language()
##I.captail()


## ? Eg:3
#polymorphism using objects

#c1, c2---->c1 = print(c1), print(c2)
#f1, f2


##class c1:
##    def f1(self):
##        print("c1") 
##
##
##class c2(c1):
##    def f1(self):
##        super().f1()
##        print("c2") 

##obj1 =c2()
##obj1.f1()

##obj2 =c1()
##obj2.f1()

##def  display(a):
##    a.f1()
##display(obj1)
##display(obj2)

# * changing the functionality of builtin functions
#a = 9
#b = 6
##print(a+b)
##print(a.__add__(b))

#print(a.__sub__(b))

##class shopping:
##    def __init__(self, l1):
##        self.items = l1
##
##    def __len__(self):
##        length = len(self.items)
##        return length
##s = shopping([1,2,3,4,5])
##print(len(s))


# ! Method overloading
# ! Eg:1
##class suming:
##    def add(self, a, b, c):
##        print(a+b)
##
##    def add(self, a, b, c):
##        print(a+b+c)
##
##s = suming()
##s.add(4, 3)
##s.add)4, 5, 1)

# ! Eg:2
##class summing:
##    def add(self, a=None, b=None, c=None):
##        if a!=None and b!=None and c!=None:
##            print(a+b+c)
##        elif a!=None and b!=None:  
##            print(a+b)
##        else:
##            print(a)
##obj= summing()
##obj.add(2)
##obj.add(3, 4)
##obj.add(1,2,3)


# ! Abstarction----------->
# The process of hiding the implimentation details is abstraction

# ? Eg:1

##def decor(func):
##    def inner():
##        srt1 = func()
##        return str1.upper()
##    return inner()
##
##def greet():
##    return 'good morning'
##print(greet)
            
##class triangle (shapes):
##    def traingle_sides(self):
##        print("3 sides")
##
##    def name(self):
##        print("Iam traingle")
##
##    def sides (self):
##        pass
##
##class square(shapes):
##        print("4 sides")
##    def sides (self):
##        pass
##
##tr triangle()
##tr.traingle_sides()
##tr.name()


# ! Rules to define abstract class1
#1.) Abstract class cannot be instantiated.
#2.) from ahc import ABC, abstractmethod
#3.) subclass the normal class with ABC
#4.) convert the normal method inside the abstract class to abstract method
#5.) all the child classes have to be subclassed with abstract class
#6.) The abstract method should be present in the
#child classes

# ? Eg:2
# super()
##from abc import ABC, abstractmethod
##class c1(ABC):
##    @abstractmethod
##    def m1(self):
##        print("This is abstract class")
##
##class c2(c1):
##    def m2(self):
##        super().m1()
##        print("I am child 1")
##
##    def m1(self):
##        pass
##
##class2 = c2()
##class2.m2()

# ? Eg:3
##from abc import ABC, abstractmethod
##class password(ABC):
##@abstractmethod
##def pwd(self):
##pswd "sidd1994$"
##class login:
##def validate(self, name, passwrd): print(name, passwrd)
##Login login()
##Login.validate()


#! Encapsulation
# *---> Eg:1
##class car:
##    __name = "BMW" # Private variable
##    print(__name)


##c1 = car()
##print(c1.name)
##c1.name = "Audi"
##print(c1.name)

# * ------> # ? Eg:2
# ? Accessing private date outing the class
##class c1:
##    __phone = '9703762889'
##
##    def display(self):
##        print(self.__phone)
##c = c1()
##c.display()

# ? Eg:3
# ? declare private method
##class class1:
##    def __m1(self):
##        print("Iam private method")
##
##    def __inti__(self):
##        self.__m1()
##
##c=class1()
##c.__m1() #error

# ? nested class
##class class1:
##    class class2:
##        name ="mani"
##
##        def display(self):
##            print(self.name)
##    obj1 = class2()
##
##obj = class1()
##obj.obj1.display()


##d1 ("shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30
##
##for val in d1:
##    if d1 [val] = min(d1.values());
##        print(val)
##
##for val in d1:
##    if d1 [val] max(d1.values()):
##        print(val)

for val in d1:
    if val.startswith('s') or val.startswith('S'):
       print(val)











