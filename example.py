a='my name is uma'
print(a)
for x in range(len(a)):
    print('letter is ' + a[x] + ' and position is ' + str(x))

l=['m','y',' ','n','a','m','e',' ','i','s',' ','u','m','a']
for x in range(len(l)):
    print(str(x)+'st value in list is: '+l[x])

a=[1,2]
print(len(a))
a.append(3)
print(a)
a.insert(1,4)
print(a)
a.append(4)
print(a)
s=max(a)
print('maximum value in the list:'+str(s))
j=min(a)
print('minimum value in the list:'+str(j))
a.remove(4)
a.append(10)
a.append(9)
a.append(5)
a.insert(0,9)
a.insert(2,23)
b=[3,4,5,6,7,8,9]
c=a and b
d=a or b
e=a|b
f=a&b
print(a)
print(b)
def listaddremove():
    a.append(12)
    a.append(19)
listaddremove()
print(a)
