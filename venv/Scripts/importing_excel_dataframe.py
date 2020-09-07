from sample_before_commit import *
f=input('Enter file name to append data: ')
if f=='fileio.txt':
    file_write(f)
elif f=='namesio.txt':
    l=[]
    l=name_print(f)
    print('values of file')
    print(l)
else:
    print('File does not exists')
b=open(f,'r')
data=b.read()
print(data)
