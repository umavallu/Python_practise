'''
class Outer:
    def __init__(self):
        print('Hello outer')
    class Inner:
        def __init__(self):
            print('hello,Inner')
        def m1(self):
            print('Method m1')
#o=Outer().Inner().m1()
# or
o=Outer()
i=o.Inner()
i.m1()

#creating inner class object with in outer class definition

class Person:
    def __init__(self):
        self.name="UmaMaheswari"
        self.dob=self.Dob()
    def display_name(self):
        print('Name :',self.name)
    class Dob:
        def __init__(self):
            self.dd='29'
            self.mm='09'
            self.yy='1987'
        def display_dob(self):
            print('Date of Birth:{}/{}/{}'.format(self.dd,self.mm,self.yy))
p=Person()
x=p.dob
p.display_name()
x.display_dob()
#------------------------------------------------------
#inner class
class Human:
    def __init__(self):
        self.name="Uma Maheswari"
        self.head=self.Head()
        self.brain=self.Brain()
    def display(self):
        print('Name:',self.name)
        print('Welcome to  meet my head and brain')
    class Head:
        def display(self):
            print('Head is working')
    class Brain:
        def display(self):
            print('YOur brain is active')
h=Human()
h.display()
h.head.display()
h.brain.display()


#--------------------------------------------------------------
#Has a relation ship
# or composition
class Processor:
    intel_gold='Intel Xeon Gold'
    intel_platinum='Intel Xeon platinum'
    def __init__(self):
        print('you are in processor class')
    def display(self):
        print('The different processors available are:{} and {}'.format(Processor.intel_gold,Processor.intel_platinum))
class Graphics_card:
    nvidia_p='Nvidia Graphics card'
    amd_p='Amd Graphics card'
    def __init__(self):
        print('you are in Graphics card class')
    def display(self):
        print('The available Graphics cards are:{} and {}'.format(Graphics_card.nvidia_p,Graphics_card.amd_p))
class  Dell:
    def __init__(self):
        print('You are in Dell class')
        self.processor=Processor()
        self.graphics=Graphics_card()
    def display(self):
        print('My Dell computer details')
        print(self.processor.intel_gold)
        print(self.graphics.amd_p)
d=Dell()
d.display()
#---------------------------------------------------
# Has -a- relation
class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getcarinfo(self):
        print('Car name : {}, Model : {} and Car\'s color:{}'.format(self.name,self.model,self.color))
class Employee:
    def __init__(self,ename,empno,car):
        self.empno=empno
        self.ename = ename
        self.car=car
    def getempinfo(self):
        print('Empno : {} ,Ename:{} '.format(self.empno,self.ename))
        self.car.getcarinfo()

c=Car('Camry','SE','grey')
e=Employee('Vijay',20,c)
e.getempinfo()

#----------------------------------------------------------------
#inheritance
#class Child(Parent):
class Parent:
    a=10
    def __init__(self):
        self.b=20
        print('parent class')
    def add(self):
        c=Parent.a+self.b
        print('sum of a static variable \'a\' and instance variable \'b\' in this example:',c)
    @classmethod
    def m2(cls):
        print('Displaying static variable in class method',cls.a)
    @staticmethod
    def m3():
        print('displaying static variable in a static method',Parent.a)
class Child(Parent):
    pass
c=Child()
print('a: {}, b:{}'.format(c.a,c.b))
c.add()
c.m2()
c.m3()

#--------------------------------------------
#INHERITANCE OR IS A RELATION
class P:
    def  __init__(self,a,b):
        print('parent constructor')
        self.a=a
        self.b=b
    def add(self):
        self.c=self.a+self.b
        print('Addition of {} and {} is {}'.format(self.a,self.b,self.c))
class C(P):
    def __init__(self,a,b):
        print('child constructor')
        super().__init__(a,b)
    def diff(self):
        if self.a>self.b:
            c=self.a-self.b
        else:
            c=self.b-self.a
        print('Difference of {} and {} is {}'.format(self.a,self.b,c))
    def product(self):
        print('Product of {} and {} is {}'.format(self.a,self.b,self.a*self.b))
    def div(self):
        print('division of {} and {} is {}'.format(self.a,self.b,self.a/self.b))

c=C(-20,30)
c.add()
c.diff()
c.product()
c.div()
'''

#-----------------------------------------------
# is a relation and has a relation
from functools import *
def product(x,y):
    z=x*y
    return z
l=[2,3,2,4,5]
ol=int(reduce(product,l))
print(ol)
