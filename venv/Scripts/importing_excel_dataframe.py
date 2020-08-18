------------------set------------------
#set operations
s={2,3,1,4,7,8,9,10}
s1={3,4,5,6}
print('s:',s)
print('s1:',s1)
s2=s.union(s1)
print('union:',s2)
s2=s.intersection(s1)
print('intersection:',s2)
s2=s.symmetric_difference(s1)
print('Symmetric Difference:',s2)
-------
s={1,2,3,4,'hi'}
print(s)
s.add('hi')
s.add('my')
s.update((7,8,9),range(10-20))
print(s)
----------
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
----------------------tuple_____________
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


-------------------------------------------
    l=[1,2,3,'hi']
l.append('uma')
print(l)
l.append(['uma'])
print(l)

-----------------------------------------------
l=[]
for i in range(100):
    if i%10==0:
        l.append(i)
    else:
        continue
print(l)
---------------------------------------------
# even and odd list till 30
s=[]
s=[i for i in range(1,31)]
print(s)
even=[i for i in s if i%2==0]
print('Even list:',even)
odd=[i for i in s if i%2!=0]
print('odd list:',odd)
--------------------------------------------------------
# first letter in each word as a seperate list
s=input('Enter string: ')
l=s.split()
print(l)
letters=[]
for i in l:
    print(type(i),i,i[0],i[:])
    letters.append([i[0],len(i)])
#letters=[i[0] for i in l]
print(letters)
print(letters[1][0])

--------------------------------------------------------------------------
l=[10,20,30,40,50,60]
l.append(70)
l.insert(1,15)
print(l)
l1=[5,15,25,35,45,55,65]
l.extend(l1)
s='hi my name is uma'
print(s.count(' '))
print(l)
l.pop(3)
l.remove(60)
print(l)
l=l+[80,90]
print(l)
l2=[110,120,130]
l2=l2+l1
print('l2 is:',l2)
l=[3,5,6,4,7,8,12,34,56,60,13,34,58,14,18]
print(l)
print(l.append(1),l)
print(l.extend([7,9]),l)
m=l.pop(4)
print('popped item: ',m,' list:',l)
n=l.remove(7)
print('Removed item: ',n,'list: ',l)
j=10
n=l.insert(4,j)
print('Inserted item is: ',j,' list is: ',l)
output=[]
for i in l:
    if i%2==0:
        output.append(i)
print('sorting list Alphabetically',output.sort(reverse=True),output)
print('Reversed sort order output.sort(reverse=True)',output.sort(reverse=True),output)
l1=[11,9,7,5,3,13,15,27]
l2=l+l1
print('adding two lists')
print('l:',l,'l1:',l1)
print('l+l1:',l2)
l1.append([10,20])
print(l1)
print(l1[-1])
l.clear()
print(l)
#copying list to another list using id
l=l1
l.append(80)
print('update list l using id:',l)
print('l1:',l1)
#copying one list to another using cloning
l=l1[0:]
l1.append(90)
print('updating list l1 using cloning:',l1)
print('l:',l)
l.append(11)
print(l)
print("no.occurances of 11 is:",l.count(11))
l=l+[20,67]
print(l)
s=[1,2,3,1,3,4,5,5,6]
print(s.count(3))
----------------------------------------------------------------------------
'''
Displaying data like below
a4b3j1u2-->aebejkuw
'''
s=input('Enter string each character followed by a number:')
output=''
k=''
for i in s:
    if i.isalpha():
        prev_chr_ord=ord(i)
        output=output+i
    else:
        output=output+chr(prev_chr_ord+int(i))
print(output)

---------------------------------------------------
#Reverse the words in a string
#method1
s=input('Enter the string:').split()
print()
s1=reversed(s)
s2=' '.join(s1)
print(s2)
#method2
#method2
s=input('enter the string:').split()
print(s)
o=''
for i in range(-1,(-len(s)-1),-1):
   o=o+s[i]+' '
print(o)

--------------------------------------------------
#displaying characters in a string at odd or even positions
s=input('Enter a string:')
odd_str=''
even_str=''
for i in range(len(s)):
       if i%2 == 0:
              even_str=even_str+s[i]
       else:
              odd_str=odd_str+s[i]
print('even positioned characters in sring \"{}\" is: {}'.format(s,even_str))
print('odd positioned characters in sring \"{}\" is: {}'.format(s,odd_str))
----------------------------------------------------------
#Reversing the string
#method1
s=input('Enter the string:')
r=reversed(s)
print(r)
print(type(r))
s1=''.join(r)
print(s1)

#method2
s=input('Enter the string:')
print(s[::-1])

#method3
s=input('Enter the string:')
r=''
i=len(s)-1
while i>=0:
       r=r+s[i]
       i=i-1;
print(r)

-----------------------------------------------------------------------
#string functions
s='My name is uma'
age='33'
print('Substring \"a\" in mainstring \"{}\" has {} occurances'.format(s,s.count('a')))
print('String \"{}\" after replacing \"a\" with \"A\" is {}'.format(s,s.replace('a','A')))
s1='   my name is     uma    '
print(s1.strip())
print(s1.find('a',0,(len(s1)+1)))
print(s1.rfind('a',0,(len(s1)+1)))
print(s1.index('a',0,(len(s1)+1)))
print(s1.rindex('a',0,(len(s1)+1)))
zip=['70503','3355']
s2='-'.join(zip)
print('zipcode is :',s2)
s3='my name is Uma Maheswari Vallu'
print('uma1234',isalnum())
print('my name is Uma Maheswari Vallu'.upper())
print('my name is Uma Maheswari Vallu'.lower())
print('my name is Uma Maheswari Vallu'.capitalize())
print('my name is Uma Maheswari Vallu'.title())
print('my name is Uma Maheswari Vallu'.swapcase())
print('UMAMAHESWARI29091987'.isupper())
print('uma1234'.islower())
print('umavallu'.isdigit())
print('12345  '.isdigit())
print('    '.isspace())
print('uma        '.isspace())
print(ord('a'))
print(len(zip))


----------------------------------------
######### not yet done
number to word
------------------------------------------------------------
s=int(input('Enter the number:'))
d={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'Nine'}
d1={11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',10:'ten'}
d2={2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eigthy',9:'ninty'}
str_num=str(s)
length=len(str_num)
if length==1:
    print("the given number is:")
    print(d.get(s))
#23//10==>2
if length==2:
    if s in d1:
        print('The given number is:')
        print(d1.get(s))
    else:
        tens_digit=s//10
        ones_digit=s%10
        print('The given number is:')
        print(d2.get(tens_digit),d.get(ones_digit))
if length==3:
        hundreds_digit=s//100
        tens_digit=s//10
        ones_digit=s%10
        print('The given number is:')
        print(d.get(hundreds_digit),' hundred',end=' ')
        if tens_digit in d2:
            print(d2.get(tens_digit),d.get(ones_digit),end=' ')
        else:
            new=int(str(tens_digit)+str(ones_digit))
            print(d1.get(new))


-------------------------------------------------------
#FINDING SUBSTRING IN MAIN STRING

name=input('enter main string:')
substring=input('enter substring:')
length=len(name)
last_idx=name.rfind(substring)
occurance=0
if last_idx==-1:
    print('substring does not exist in the main string')
else:
     occurance=occurance+1
     i=0
     while i<last_idx-1:#0 to 3
        index_i=name.find(substring,i,last_idx-1)
        if index_i==-1:
            break
        else:
            occurance=occurance+1
            i=index_i+len(substring)
print('Total no of occurances :',occurance)
----------------------------------------------------
#function with unknown arguments
def student(*childnames):
    print(childnames)
    x=0
    for i in childnames:
        x=x+1
        print('{} child name is {}'.format(x,i))
student('ADITHYA','PRADYUMNA','VIJAY','UMA')


------------------------------------------------------------------
#printing characters in a string using both positive and negative indexing

a=[10,20,30,40,50,]
print(a,len(a))
del a[0]
print('List values are:')
i=0
while i<len(a):
    print(a[i],end=' ')
    i=i+1
else:
    print('List is completed')

--------------------------------------------------------------------------
s=input('Enter any string:')
for i in range(len(s)):
    if len(s) != 0:
        print('character at positive index {}, and negative index {} is,{}'.format(i,(i-len(s)),s[i]))
    else:
        print('Empty string cant display characters')
else:
    print('All string characters are displayed')

--------------------------------------------------------------------

'''
1
1 2
1 2 3
1 2 3 4
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''

n=int(input('enter a number:'))
for i in range(n):
    for j in range(n):
        print(j+1,end=' ')
    print()
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

n=int(input('enter a number:'))
for i in range(0,n):
    for j in range(0,i+1):
        print(i+1,end=' ')
    print()


'''
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''
#fourth

n=int(input('enter a number:'))
for i in range(n):
    for j in range(n):
        print(i+1,end=' ')
    print()

'''
*
* *
* * *
* * * *
* * * * *
'''
n=int(input('enter a number:'))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()

'''
# first logic
#second

#third


--------------for loop ------------------------
a=eval(input('enter list:'))
print(a)
print(type(a))
sum=0
for i in range(0,len(a),1):
    sum=sum+a[i]
    if a[i]==30:
        print('current value in loop is,{} so the loop continues'.format(a[i]))
        continue
    if a[i]==60:
        print('current value in loop is,{} so the loop breaks'.format(a[i]))
        break
print('sum:',sum)
sum_neg_idx=0
b=-len(a)
for i in range(-1,-len(a)-1,-1):
    sum_neg_idx=sum_neg_idx+a[i]
print('sum with negative indexing:',sum_neg_idx)


-------Flow control-----------------------------

vijay='father'
uma='mother'
bigbro='adithya'
littlebro='pradyumna'
family_mem=input('enter the person you want to meet:')
if family_mem =='father':
    print('Hi vijay')
elif family_mem =='mother':
    print('Hi uma')
elif family_mem =='bigbro':
    print('Hi adithya')
else:
    print('Hi Pradyumna')


string formatting-------------------------

a=1.5
a=int(a)
b=5
c=10
s='i have paid {2}dollars for {0}masks\",\"instead i got {1}masks'
print(s.format(a,b,c))

o/p:
i have paid 10dollars for 1masks","instead i got 5masks
-------------------------

print('        my name is uma'.strip(' '))
print('my name is uma'.upper())
print('my name is uma'.lower())

print('my\nname\nis\numa')
print('my name is uma'.split(' '))
print('my_name_is_uma'.split('_'))
print('my**name**is**uma'.split('**'))

o/p:
my name is uma
MY NAME IS UMA
my name is uma
my
name
is
uma
['my', 'name', 'is', 'uma']
['my', 'name', 'is', 'uma']
['my', 'name', 'is', 'uma']


-----------argv command line args-- argv[0] is the file name
 from sys import argv
username,password=argv[1],argv[2]
print('Filename:',argv[0])
print(username)
print(password)

split()-------------------------------------return space seperated input into a list

one-------------
a=input('values:').split()
print(a)
o/p:
values:a b c d
['a', 'b', 'c', 'd']==<list
two---------------
a=input('values:').split(',')
print(a)
o/p:values:a,b,c,d,e,f
['a', 'b', 'c', 'd', 'e', 'f']

three------------
a=input('enter more than one value seperated by single space').split()
print(a)
s=0
for i in range(len(a)):
    s=s+int(a[i])
print('sum of values in list is:',s)

i/p:-- 1 2 3 4
o/p: a=['1','2','3','4']
sum==10
-----------------------------------------
List comprehension
a=[int(i) for i in input('enter morethan one value:').split()]

-----------------------------------------------------------
even=[2,4,6,8,10]
odd=[1,3,5,7,9]


def authentication(username,password):
  username=input('Enter Username: ')
  password=input('Enter Password: ')
  if upper(username)=='UMA' and upper(password)=='UMA':
      print(' User is valid ')
  else:
      print(' User is not valid ')

def area_of_circle(radius):
    radius=int(input('Enter radius: '))
    pi=3.14
    area=pi*(radius**2)
    print(' Area is: ',area)

---- creating list runtime
i=int(input('How many valuews you want in list:'))
l=[]
for x in range(i):
    z=input('Enter value to add in the string list')
    if z in l:
        print(z,' is already in list, do not append')
    else:
        print(z," is not in the list, plz add")
        l.append(z)
print(l)

-----

username = input('Enter Username:')
password = input('Enter Password')
if username == 'uma' and password == 'maheswari':
    print('access granted')
else:
    print('access denied')

-------
operators

a = 10.0
b = 5
print(a + b)  # adding two operands
print(a - b)  # subtracting one operand from another
print(a * b)  # multiply
print(a / b)  # division
print(a ** b)  # exponents a power b
print(a // b)  # floor division
print(a % b)  # reminder
print(a and b)  # if a is true==>b ,a is false==>a
print(a or b)  # if a is true==>a, b is false b
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a | b)
print(a & b)

answers: 15, 5, 50, 2.0, 100000, 2, 0
5, 10,
False, True, False, True, 15, 0

1.
arithmatic
operators - -
+, -, *, /, **, //, %

a = 10
b = 5
print(a + b)  # adding two operands
print(a - b)  # subtracting one operand from another
print(a * b)  # multiply
print(a / b)  # division
print(a ** b)  # exponents a power b
print(a // b)  # floor division
print(a % b)  # reminder operator

a='my name is uma'
---------------------------------------------------------------------------------------------------------------------

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
---------------------------------------------------------------------------------------------------------------------------
#odd or even
for x in range(11):
    y=int(x%2)
    if y==0:
       print(str(x)+'is even')
    else:
        print(str(x)+'is odd')

#-----------------------------------------------------------------------------------------------------------------------------
def lessthan100(a,b):
    if a<100 and b<100:
            c=True
            return c

lessthan100(10,20)

# appending to list
z=[1,2,3,4]
def listaddremove():
    z.append(12)
    z.append(19)
listaddremove()
print(z)

#odd or even
for x in range(11):
    y=int(x%2)
    if y==0:
       print(str(x)+'is even')
    else:
        print(str(x)+'is odd')

#vowels
x = input('Enter string:')
print(x[0])
def vowelcnt():
    v=0
    for i in range(len(x)):
        if x[i]=='a' or x[i]=='e' or x[i]=='i' or x[i]=='o' or x[i]=='u':
            v=v+1
    return v
print(x)
y=vowelcnt()
print('No of vowels in the string: '+x+' is '+str(y))
----_----------------------------------------------------------------------------------------------

Finding min and max using ternary operators
#ternary operators
a=int(input('enter the first number:'))
b=int(input('Enter the 2nd number:'))
c=int(input('Enter the 3rd number:'))
d= a if a<b & b<c else b if b<c else c
print('Minimum number among these',a,b,c,'is',d)

#finding minimum value using ternary operators
a=int(input('enter the first number:'))
b=int(input('Enter the 2nd number:'))
c=int(input('Enter the 3rd number:'))
d= a if a>b & b>c else b if b>c else c
print('Maximum number among these',a,b,c,'is',d)

#maximum and minimum values using max() and min() functions
a=int(input('enter the first number:'))
b=int(input('Enter the 2nd number:'))
c=int(input('Enter the 3rd number:'))
d=max(a,b,c)
e=min(a,b,c)
print('Maximum number among these',a,b,c,'is',d)
print('Minimum number among these',a,b,c,'is',e)

#ternary operators---displaying string according to number values
a=int(input('enter the first number:'))
b=int(input('Enter the 2nd number:'))
s1='First value is large'
s2='second value is large'
s3='Both the values are equal'
s4=s3 if a==b else s2 if a<b else s3
print(s4)