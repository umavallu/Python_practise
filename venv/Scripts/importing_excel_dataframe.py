'''
import sys
t=eval(input('enter values for tuple:'))
print(t)
print(type(t))
l=[1,2,3,4]
print(l)
print(type(l))
print(sys.getsizeof(t))
print(sys.getsizeof(l))

#comparing tuples
t1=(1,2,3,4)
t2=(1,2,3,4)
t3=(4,3,2,1)
print(t1,'==',t2,' is ',t1==t2)
print(t1,'==',t3,' is ',t1==t3)
print(t1,'>',t3,' is ',t1>t3)
'''
#counting elements in tuple,ordering

print('(2,3,4,5,4,3,2,1,4,3,4,6,7) count of 4 is ',(2,3,4,5,4,3,2,1,4,3,4,6,7).count(4))
tuple_l=tuple(sorted((5,3,2,23,6)))
print('(2,3,4,5,4,3,2,1,4,3,4,6,7) Reverse sorting ',tuple_l)

