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
#write a program to create a dict with each letter as key, and occurance as the value
#METHOD1
s=input('Enter any word: ')
d={}
for i in s:
    if  i not in d.keys():
        d[i]=1
        #print(i,'does not exists in ',d)
    else:
        d[i]=d[i]+1
        #print(i, 'exists in ',d)
print(d)
#METHOD2(using dict.get(key,defaultvalue)
s=input('Enter any word: ')
d={}
for i in s:
    d[i]=d.get(i,0)+1
#for k,v in d.items():
#    print('Key : ',k,' Value : ',v)
print(d)
#popping all the values in the dict
#method1(keys())
l=list(d.keys())
for i in l:
    d.pop(i)
print(d)
#method2(items())
key_value=list(d.items())
for i in key_value:
    d.pop(i)
print(d)
#using setdefault(key,value)
d={1:'uma',2:'vijay',3:'adithya'}
print(d)
print(d.setdefault(4,'pradyumna'))
print(d.setdefault(1,'mahee'))
print(d.setdefault(5,'uma'))
print(d)

#collection merging

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
d={'maths':100,'science':80,'social':58,'hindi':76,'telugu':86,'english':56}
print(d)
sum_of_values=sum(d.values())
print('Student score is: ',sum_of_values)
####nested dict
dnested={'student1':{'name':'uma','marks':[84,76,56,86,65,53]},
         'student2':{'name':'vijay','marks':[89,79,64,90,76,79]}
 }
for key,value in dnested.items():
    print('key: ',key,' value: ',value)

d_nested={'student1':'uma','marks_uma':{'maths':100,'science':80,'social':58,'hindi':76,'telugu':86,'english':56},
          'student2':'vijay','marks_vijay':{'maths':89,'science':76,'social':79,'hindi':79,'telugu':89,'english':64}
          }
for key,value in d_nested.items():
    print('key: ',key,' value: ',value)
print('value of marks vijay:',d_nested['marks_vijay']['english'])
