import sys
a=sys.argv[1:]
print('Argument list is:',a)
print(type(a))
sum=0
for i in a:
        n=int(i)
        print('i:',i,'n:',n)
        sum=sum+n
print('sum:',sum)