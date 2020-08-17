'''
s={1,2,3,4}
s1=s.copy()
s.add(5)
print(id(s),'     ',id(s1))
print(s is s1)
l=[1,2,3,4,5]
l1=l.copy()
l1.append(8)
print(id(l),'     ',id(l1))
print(l,'    ',l1)
print(l is l1)
print(s==s1)
#removing duplicates from set
#method1
s3={1,2,3,4,5,6,6,7,1,2,3,5,8,9,10,3,4}
s4=set()
for i in s3:
    if i not in s4:
        s4.add(i)
print(s4)
#method2(set automatically delete duplicates)
s3={1,2,3,4,5,6,7,2,3,4,5,6,7,8,9,1,2,3,4,5,6,9,8,10,30}
s4=s3
print(s4)
'''
s={1,2,3,'hi',4.5,(6,7,8)}
for i in range(len(s)):
    if len(s) != 0:
        s.pop()
        print(s)

'''
s={1,2,3,4,'hi',(1,2,34,7)}
#Removing all the elements from set
#method1 using pop()
l=s.copy()
for i in l:
    if i in s:
        s.pop()
print(s)

#method2 using remove(i)
s={1,2,3,4,'hi'}
l=s.copy()
for i in l:
    if i in s:
        s.remove(i)
print(s)
'''