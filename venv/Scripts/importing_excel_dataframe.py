#positional arguments
def multiplication_table(a):
  for i in range(1,21):
      print('{} * {} = {}'.format(a,i,a*i))
multiplication_table(1) # 1 is the positional argument
multiplication_table(2) # 2 is the positional argument
multiplication_table(3) # 3 is the positional argument
# Finding Factorial
#Method1
def factorial(a):
    fact_value=a
    i=a
    while i>1:
        fact_value=fact_value*(i-1)
        i=i-1
    return fact_value
print('Factorial value of 3 is:',factorial(3))
#Method2
def factorial(a):
    fact_value=a
    if a !=1:
        fact_value=fact_value*factorial(a-1)
    return fact_value
print('factorial of 4 is :',factorial(4))
#Returning multiple values
def arithmetic_op(a,b): #def arithmetic_op(a,b=1)--> no error and def arithmetic_op(a=10,b)---> error
    add_value=a+b
    diff_value=(a-b if a>b else b-a)
    mul_value=a*b
    div_value=a/b
    exp_value=a**b
    return add_value,diff_value,mul_value,div_value,exp_value
a,b,c,d,e=arithmetic_op(10,4) #a,b,c,d,e=arithmetic_op(10,b=4)=> no error and a,b,c,d,e=arithmetic_op(a=10,4)-->error
print('Addition of 10 and 4 is:',a)
print('Difference of 10 and 4 is:',b)
print('10*4 is:',c)
print('10/4 is:',d)
print('exponential value of 10 and 4 is:',e)

#default arguments
def sum(a,b=5):
    sum=a+b
    print('Total of {} and {} is: {}'.format(a,b,sum))
sum(a=6,6)

#variable length arguments
#variable length argument with *
def tuple_dict(*args,n):
    sum,total=0,0
    for i in args:
        sum=sum+i
    total=sum+n
    return total,sum
total,sum=tuple_dict(10,20,30,40,n=100)
print('total: ',total,' sum: ',sum)
#variable length arguments with * and **
def tuple_dict(*marks,**stu_details):
    score=0
    for i in marks:
        score=score+i
    j=stu_details.items()
    return score,j
d={}
total,d=tuple_dict(10,20,30,40,50,name='uma',school='saikrishna',class_name='board')
for k,v in d:
    print(k,' : ',v)
print('score: ',total)
#Function with unknown number of arguments
def tuple_sum(*l):
    sum=0
    for i in l:
        sum=sum+i
    return sum
print('tuple_sum([1,2,3,4,5] : ',tuple_sum(1,2,3,4,5))
#Function to add elements in list(created using list comprehension)
j=[int(i) for i in input('enter list:').split(',')]
print(j)
def list_collection_sum(l):
    sum=0
    for i in l:
        sum=sum+i
    return sum
print('sum of {} is : {}'.format(j,list_collection_sum(j)))