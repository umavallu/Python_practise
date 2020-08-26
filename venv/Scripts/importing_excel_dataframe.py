#working with map() and lambda() to assign each list value with doubled value
def twice(num):
    double=num*2
    return double
l=[1,2,3,4,5,6,7,8,9,10,11]
l2=list(map(twice,l))
print('2 table for the given list:',l2)
#3table
l3=list(map(lambda x:x*3,l))
print('3 table for the given list is:',l3)
#Lambda Functions
#to find squares
s= (lambda x:x*x)
print('Square of {} is {} ',4,s(4))
print('Square of {} is {} ',10,s(10))
#to find sum of two numbers
sum=(lambda a,b:a+b)
print('Addition of 7 and 8 is:',sum(7,8))
print('Addition of 29091987 and 3 is:',sum(29091987,3))
#to find whether a number is even or odd
even_odd= (lambda x:'Even' if x%2==0  else 'Odd')
print('Is 8 even/odd: ',even_odd(8))
print('Is 59 even/odd: ',even_odd(59))


#working with filter() and lambda()
#Here iseven is taking each element in list l as an argument and return True/False
#Filter function returns each list value which is True
def iseven(num):
    if num%2==0:
        return True
    else:
        return False
l=[int(i) for i in input('enter values for list: ').split(' ')]
print(l)
l1=list(filter(iseven,l))
print('Even list of {} is :{}'.format(l,l1))
l2= list(filter((lambda x: True if x%2!=0 else False),l))
print('Odd list of {} is :{}'.format(l,l2))

#Accessing global values globals()['variablename']
a=10
def f1(x):
    a=20
    print('Product of {} and {} is: {} '.format(a,x,x*(globals()['a'])))
def f2(x):
    print('Addition of {} and {} is: {}'.format(a,x,x+a))
f1(2)
f2(2)