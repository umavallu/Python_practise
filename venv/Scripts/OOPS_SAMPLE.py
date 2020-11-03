
#Creating file with the given name
name=input('Enter filename to create:')
f=open('C:\\Users\Vijay\\PycharmProjects\\untitled\\venv\\Scripts\\'+name+'.txt','w')
f.write('Hi')
f.write(' uma')
f.write(' maheswari\n')
f.write('My elder son\'s name is Adithya\n')
f.write('My younger son\'s name is Pradyumna\n')
f.write('My husband\'s name is Vijay')
f.close()
f=open('C:\\Users\Vijay\\PycharmProjects\\untitled\\venv\\Scripts\\'+name+'.txt','r')
data=f.readlines()
for i in data:
    print(i)
print(data)

# Writing data from list to a file and accessing multiple lines
l=['Uma',"Vijay","Adithya","Pradyumna"]
f=open('sample.txt','w')
for i in l:
    f.write(i+'\n')
f.close()
f_read=open('sample.txt','r')
read=f_read.readlines()
for i in read:
    print(i,end='')

#Writing Multiple lines in the file
#Using Exception handling for FileNotFound Exception
try:
    l=["Uma\n","Vijay\n","Adithya\n",'Pradyumna\n']
    f=open('sample.txt','w')
    print('File Name:',f.name)
    print('File is opened to Read(Y/N):',f.readable(),' Write(Y/N):',f.writable())
    f.writelines(l)
    f.close()
    print('Is File closed(Yes/No):',f.closed)
    f=open('sample.txt','r')
    data=f.readlines()
    for i in data:
        print(i,end='')
except FileNotFoundError as msg:
    print(msg)

#Copying from one file to another

try:
    f=open('sample.txt','r')
    f1=open('sample1.txt','w')
    data=f.read()
    f1.write(data)
    f.close()
    f1.close()
    f1=open('sample1.txt','r')
    data_f1=f1.read()
    print(data_f1)
except FileNotFoundError as msg:
    print(msg)
finally:
    f1.close()

#using seek and tell
f=open('sample.txt','r')
print(f.tell())
print(f.seek(10))
n=f.read()
print(f.tell())
print(n)
f=open('sample.txt','r')
f.seek(0)
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.readline())
print(f.tell())
print(f.read(6))
print(f.tell())

#Using with, seek and tell
#with open('sample.txt','r') f:
data="Hi very good morning"
f=open('abc.txt','w')
f.write(data)
with open('abc.txt','r+') as f:
    text=f.read()
    print(text)
    print('Current cursor position: ',f.tell())
    f.seek(3)#from 3rd position pvm will start replacing given data
    print('Current cursor position: ', f.tell())
    f.write('friends!!')
    print('Current cursor position: ', f.tell())
    f.seek(0)
    text=f.read()
    print('Contents of the file after modification')
    print(text)

#Checking whether particular file exists or not
#Using os library, isfile() function (os.path.isfile(filename)
import os,sys
fname=input('Enter file name:')
if os.path.isfile(fname):
    print('File exists')
    f=open(fname,'r')
else:
    sys.exit(0)
data=f.read()
print(data)

#Program to print characters,words and lines present in the given file
import os,sys
fname=input('Enter file name:')
if os.path.isfile(fname):
    print('File exists')
    f=open(fname,'r')
else:
    sys.exit(0)
data=f.read()
print(data)
f.seek(0)
lines=f.readlines()
lcount=ccount=wcount=0
for line in lines:
    lcount+=1
    ccount+=len(line)
    words=line.split()
    wcount+=len(words)
print('Number of lines:',lcount)
print('Number of words:',wcount)
print('Number of characters:',ccount)

#Read image file and write into a new image file
f1=open('IMG_0005.JPG','rb')
f2=open('Adithya.jpg','wb')
data=f1.read()
f2.write(data)
print('New image is available with the name Adithya.jpg')

#Comma seperated Value File(CSV)

import csv
with open('sample_csv.csv','w') as f:
    w=csv.writer(f)
    w.writerow(['Eno','Ename','Esal','EAddr'])
    for i in range(5):
        l=input('Enter values for eno,ename,esal,eadd seperated by comma:').split(',')
        w.writerow(l)
    print('Employess added to the sample_csv.csv file')

#CSV File with out printing new line after each inserted line
import csv
with open('Employee.csv','w',newline=' ') as f:
    w=csv.writer(f)
    f.writerow(['EmpNo','Ename','Sal','Designation','Deptno'])
    n=int(input('Enter how many employee details you want to insert:'))
    for i in range(n):
        l=input('Enter (Empno,Ename,Sal,Designation,Deptno) separated by space').split(' ')
        f.writerow(l)
f.close()

#zipping and unzipping of files

from zipfile import *
f=ZipFile('zip_file.zip','w',ZIP_DEFLATED)
f.write('namesio.txt')
f.write('sample.txt')
f.write('sample_csv.csv')
print('Zipping of files is done')
f.close()

#unzipping of files
from  zipfile import *
f=ZipFile('zip_file.zip','r',ZIP_STORED)
files_list=f.namelist()
for i in files_list:
    print('Name of file:',i)
    print('Contents of the File:\n')
    f=open(i,'r')
    print(f.read())
    print()
    f.close()


#Working with directories(making dir,removing directories,list the contents of a directory)
import os
current_dir=os.getcwd()
print('Currently working in ',current_dir,' directory')
dir_name=input('Enter name for directory to create:')
os.mkdir(dir_name)
print('New dir ',dir_name,' created')
os.makedirs('dir1/dir2/dir3')
print('Dirs created')
os.rmdir('dir2/dir3')
print('Directory dir3 removed')
