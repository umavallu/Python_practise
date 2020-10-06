

############
#Interface
#an abstract class with only abstract methods
##########################
#abstraction
####################
#abstract method with out child class
#with abstract class
#scenario 1
#cant instantiate for abstract class with abstract method(which is incomplete)
'''
from abc import abstractmethod,ABC
class Parent(ABC):
    @abstractmethod
    def m1(self):
        pass
p=Parent()
p.m1()
#Abstract class with completed abstract method
#scenario 2
from abc import abstractmethod,ABC
class Parent(ABC):
    @abstractmethod
    def m1(self):
        print('HI Everybody')
p=Parent()
p.m1()
#abstract method(use abstract decorator,which u need to import for abc(abstract base class module) module)
#it will not throw error bcz u dint inherit from abstract class ABC
#here Abstact_method class is abstract class
#scenario 3

from abc import abstractmethod
class Abstract_method:
    @abstractmethod
    def m1(self):
        pass
a=Abstract_method()

#Scenario 4
#ABstact parent class with abstract child class
#cant instantiate
from abc import abstractmethod,ABC
class Parent(ABC):
    @abstractmethod
    def m1(self):
        pass
class Child(Parent):
    pass
c=Child()
# abstract method in abstract class with concrete child class
from abc import abstractmethod,ABC
class Parent(ABC):
    @abstractmethod
    def m1(self):
        pass
class Child(Parent):
    def m1(self):
        print('Hello')
c=Child()
c.m1()
#Child class inherited from abstract class interface
from abc import abstractmethod,ABC
class Vehicle(ABC):
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod
    def tyres(self):
        pass
    @abstractmethod
    def battery(self):
        pass
class Car(Vehicle):
    def engine(self):
        print('My Car engine is OPOC')
    def tyres(self):
        print('My car tyres are TOYO Open Country')
    def battery(self):
        print('MY car battery is Diehard Platinum')
c=Car()
c.engine()
c.tyres()
c.battery()


# Abstract class with both abstract and non abstract methods

from abc import abstractmethod,ABC
class Vehicle(ABC):
    @abstractmethod
    def engine(self):
        pass
    def tyres(self):
        print('My car tyres are TOYO Open Country')
    def battery(self):
        print('MY car battery is Diehard Platinum')
class Car(Vehicle):
    def engine(self):
        print('My Car engine is OPOC')
c=Car()
c.engine()
c.tyres()
c.battery()
###################
# polymorphism
###############
#overriding
class Father:
    def input_name(self,name):
        self.name=name
    def display(self):
        print('Father\'s name is: ',self.name)
class Mother(Father):
    def display(self):
        #super().input_name('koteswararao')
        super().display()
        print('Mother\'s name is: Ramadevi')
m=Mother()
m.input_name('koteswararao')
m.display()


#sample overloading
class Duck:
    def m1(self):
        print('Quack')`12wedfv 
class Cat:
    def m1(self):
        print('Meow')
class Dog:
    def m1(self):
        print('Bow wow')
class Cow:
    def m1(self):
        print('Moo')
l=[Duck(),Cat(),Dog(),Cow()]
for i in l:
    i.m1()

#same class objects 
#<,>,<=,>=
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def score(self):
        total=0
        for i in self.marks:
            total=total+i
        self.total_marks=total
    def display(self):
        print('Name:',self.name)
        print('Score:',self.total_marks)
    def __gt__(self,other):
        return self.total_marks>=other.total_marks
    def __le__(self,other):
        return self.total_marks<=other.total_marks

s=Student('Uma',[98,67,87,98,89,100])
s.score()
s.display()
s1=Student('Vijay',[89,90,98,78,89,78])
s1.score()
s1.display()
print(s.name,' gets more marks than ',s1.name,':',s>s1)
print(s.name,' gets less marks than ',s1.name,':',s<s1)
print(s.name,' gets more marks than ',s1.name,':',s>=s1)
print(s.name,' gets more marks than ',s1.name,':',s<=s1)

#multiplication
class  Car:
    def __init__(self,carmodel,price,company):
        self.carmodel=carmodel
        self.price=price
        self.company=company
    def display(self):
        print('Car Details')
        print('Model:',self.carmodel)
        print('Price:',self.price)
        print('Company:',self.company)
    def __mul__(self,other):
        return self.price*other.emi_percent
class EMI:
    def __init__(self,emi_percent,duration):
        self.emi_percent=emi_percent
        self.duration=duration
    def __mul__(self,other):
        return (self.emi_percent*100)*other.duration
c=Car('SE',15000.00,'Toyota')
if hasattr(c,'display'):
    c.display()
else:
    print('Display() method does not exist')
e=EMI(0.0183,55)
print('The monthly payment for car:',c*e)
print('Total emi payment:',e*e)


#############
#super() method to access parent class variables, methods and constructors
class Parent:
    job='yes'
    def __init__(self,name,city,married):
        self.name=name
        self.city=city
        self.married=married
    def info(self):
        print('Hi, my name is ',self.name)
        print('Currently iam staying in ',self.city)
        print('Iam ',self.married)
    @classmethod
    def jobinfo(cls):
        print('Iam ',cls.job)

class Child(Parent):
    job='no'
    def __init__(self,name,city,married,cname,cage):
        super().__init__(name,city,married)
        self.cname=cname
        self.cage=cage
    def info(self):
        super().info()
        super().jobinfo()
        print(super().job,self.name)
        print(self.cname,'is ',self.job,' working')
c=Child('uma','lafayette','yes','adithya',8)
c.info()



#MRO Example 2
class D:
    def m1(self):
        print('D class')
class E:
    def m1(self):
        print('E class')
class F:
    def m1(self):
        print('F class')
class B(D,E):
    def m1(self):
        print('B class')
class C(D,F):
    def m1(self):
        print('C class')
class A(B,C):
    def m1(self):
        print('A class')
        super().m1()
a=A()
a.m1()
print(A.mro())

#               a
#           /       \
#          b          c
#           \       /
#               d
# Method Resolution Order or mro()
#Classname.mro()
class a:
    def m1(self):
        print('a class')
class b(a):
    def m1(self):
        print('b class')
class c(a):
    def m1(self):
        print('c class')
class d(b,c):
    def m1(self):
        print('d class')
print(a.mro())
print(b.mro())
print(c.mro())
print(d.mro())


#Multiple Ingeritance
#    a              b
#       \       /
#           c
class Parent1():
    def add(self,a,b):
        self.c=a+b
        print('sum of ',a,' ',b,' is:',self.c)
    def m1(self):
        print('hello Parent1')
class Parent2():
    def sub(self,a,b):
        #c=a-b if: a>b else b-a
        if a>b:
            self.c=a-b
        else:
            self.c=b-a
        print('Subtraction of ',a,' ',b,' is ',self.c)
    def m1(self):
        print('Hello Parent2')
class Child(Parent1,Parent2):
    pass
c=Child()
c.m1()
c.add(4,5)
c.sub(9,4)
print(Child.mro())

# Hierarchical Inheritance
class Parent:
    def __init__(self):
        print('Welcome to hierarchical inheritance parent')
    def m1(self):
        print('parent method')
class Child1(Parent):
    def __init__(self):
        print('Inheriting from parent resource to child1')
        super().__init__()
class Child2(Parent):
     pass
c=Child1()
c.m1()
c1=Child2()
c.m1()


#multilevel inheritance
class Parent:
    def __init__(self):
        print('level1')
    def m1(self):
        print('Hi iam parent method')
class Child(Parent):
    def __init__(self):
        print('level2')
        super().__init__()
    def m2(self):
        print('Hi iam child method')
class SubChild(Child):
    def m3(self):
        print('Iam subchild method')
cc=SubChild()
cc.m1()
cc.m2()
cc.m3()
########################
'''