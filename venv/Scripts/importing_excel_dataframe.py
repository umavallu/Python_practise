###############################################
# wap to read names and marks for dict and print them
d={}
l=int(input('Enter how many student records u want to enter:'))
for i in range(l):
    name=input('Enter student name: ')
    marks=int(input('Enter student marks in percentage: '))
    d[name]=marks
for i in d.items():
    print(i)
################################################################
#accessing elemets
d={1:'one',2:'two',3:'three',4:'four',5:'five'}
print(d)
d[1]='ONE'
print(d)
del d[1]
#del d[6]
print(d)
del d
#print(d)
#################################################################
#creating a dict with other sequences
#method1
d=dict({(1,'one'),(2,'two'),(3,'three')})
print(d)
#method2
d=dict([(1,'one'),(2,'two'),(3,'three')])
print(d)
#################################################################
#working with dict len(),clear(),get(),get(key,default value),pop(),popitem()
d=dict([(1,'one'),(2,'two'),(3,'three')])
print(d)
print(len(d))
print(d.get(1))
print(d.get(5,'five'))
print(d)
print(d.get(7))
s=d.pop(1)
print('popped item: ',s)
#print(d.pop(9))
print(d)

#collection
#collection
'''list and tuple --yes
tuple and tuple
list and list
set and list
set and tuple
'''
l=[1,2,3,4]
t=(4,5,6,7)
lt=(*l,*t)#list and tuple--> tuple
print(lt)
s={10,20,30,40}
s1={(2,3),(4,5),(6,7),(8,9)}
ll=[*l,*l]#list and list--> list
print('list and list',ll)
lsl=[*l,*s]#list and tuple--> tuple
print('list and set',lsl)
ts={*t,*s}#tuple and set-->set
print('tuple and set',ts)
lss={*l,*s}#list and set--> set
print('list and set',lss)
tst=(*t,*s)#tuple and set-->tuple
print('tuple and set',tst)
ls1l=[*l,*s1]#list and tuple--> tuple
print('list and set',ls1l)
ts1={*t,*s1}#tuple and set-->set
print('tuple and set',ts1)
ls1s1={*l,*s1}#list and set--> set
print('list and set',ls1s1)
ts1t=(*t,*s1)#tuple and set-->tuple
print('tuple and set',ts1t)
#dict works with only dict??
d={1:'one',2:'two',3:'three'}
d1={1:'hi',4:'four'}
dd1={**d,**d1}
print(dd1)
#zipping of sequences
l3=zip(l,t)
l4=list(l3)
print(l4)
s= ((6, 7), (8, 9), (10, 11), 12)
l3s=list(zip(l,s))
print(l3s)
l4d=dict(zip(d,l))
print(l4d)