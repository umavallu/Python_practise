
#Inter thread communication
#Queue Based

#Example2
from threading import *
import time
import queue
import random
q=queue.Queue()
def producer(q):
    i=1
    while i<=5:
        i=i+1
        item=random.randint(1,100)
        print('Producer is producing item :',item)
        q.put(item)
        print('Producer giving notification')
        time.sleep(5)
def consumer(q):
    i=1
    while i<=5:
        print('Consumer waiting for notification')
        if q.empty():
            print('Queue is empty and waiting for producer to produce items')
        print('Consumer consumed the item:',q.get())
        i=i+1
        time.sleep(5)
t=Thread(target=producer,args=(q,))
t1=Thread(target=consumer,args=(q,))
t.start()
t1.start()
'''
#example:-1
import threading
import time
import queue
import random
def producer(q):
    i=1
    while i<=5:
        a=random.randint(1,100)
        print('Producer is producing item: ',a)
        q.put(a)
        i=i+1
    print('Producer is giving notification')
def consumer(q):
    time.sleep(2)
    i=1
    print('Consumer is appending items to the list')
    while i<=5:
        l.append(q.get())
        i+=1
q=queue.Queue()
t=threading.Thread(target=producer,args=(q,))
t1=threading.Thread(target=consumer,args=(q,))
l=[]
t.start()
t1.start()
t1.join()
print(l)

#Lock() Rlock() and Semaphore()
#example with Lock() only one thread at a time

from threading import *
import time
l=Lock()
def display(name):
    l.acquire()
    time.sleep(3)
    for i in range(5):
        print(name,'Hi gud morning')
    l.release()
    print('Thread Name:',current_thread().getName(),'Thread identification is:',current_thread().ident)
t=Thread(target=display,args=('Uma',))
t1=Thread(target=display,args=('Vijay',))
t2=Thread(target=display,args=('Adithya',))
t3=Thread(target=display,args=('Pradyumna',))
t.start()
t1.start()
t2.start()
t3.start()
list_threads=enumerate()
print('Thread whhich is executing here is :',current_thread().getName())
for i in list_threads:
    print('Thread is:',i)

# same Example with RLock()

from threading import *
import time
l=RLock()
def display(name):
    l.acquire()
    time.sleep(3)
    for i in range(5):
        print(name,'Hi gud morning')
    l.release()
    print('Thread Name:',current_thread().getName(),'Thread identification is:',current_thread().ident)
t=Thread(target=display,args=('Uma',))
t1=Thread(target=display,args=('Vijay',))
t2=Thread(target=display,args=('Adithya',))
t3=Thread(target=display,args=('Pradyumna',))
t.start()
t1.start()
t2.start()
t3.start()
list_threads=enumerate()
print('Thread whhich is executing here is :',current_thread().getName())
for i in list_threads:
    print('Thread is:',i)
#Using Semaphore

from threading import *
import time
l=Semaphore()
def display(name):
    l.acquire()
    for i in range(5):
        time.sleep(3)
        print(name,'Hi gud morning')
    l.release()
    l.release()
    print('Thread Name:',current_thread().getName(),'Thread identification is:',current_thread().ident)
t=Thread(target=display,args=('Uma',))
t1=Thread(target=display,args=('Vijay',))
t2=Thread(target=display,args=('Adithya',))
t3=Thread(target=display,args=('Pradyumna',))
t.start()
t1.start()
t2.start()
t3.start()
list_threads=enumerate()
print('Thread whhich is executing here is :',current_thread().getName())
for i in list_threads:
    print('Thread is:',i)


# Synchronization
# 1.Lock
from threading import *
def display(numbers):
    l.acquire()
    sum=0
    for i in numbers:
        a=i
        sum=sum+a
    l.release()
    print('Sum :',sum)
l=Lock()
numbers=[5,10,15,20,25,30]
t=Thread(target=display,args=(numbers,))
t1=Thread(target=display,args=(numbers,))
t2=Thread(target=display,args=(numbers,))
t.start()
t2.start()
print('list of active threads : ',active_count())
t1.start()
print(current_thread().getName())
print(current_thread().isDaemon())

# Daemon Threads
#------------------------------------------------
# Daemon Thread

from threading import *
import time
import datetime
def display():
    for i in range(5):
        print('Lazy thread')
        time.sleep(2)
t=Thread(target=display)
#t.setDaemon(True)# if u make the thread t Daemon then output will be lazythread three times and main thread statement
t.start()
time.sleep(5)
print('Main thread exiting the program at:',datetime.datetime.now())

#ident,is_alive() or isAlive(),thread_count()
# ident
from threading import *
import time
def doubles():
    for i in range(3):
        time.sleep(5)
        print(current_thread().getName(),current_thread().ident,' is ended')
t=Thread(target=doubles)
t1=Thread(target=doubles)
t.start()
t1.start()
print('Active threads:',active_count())
list_of_threads=enumerate()
t.join(3)
print('Active threads:',active_count())
for i in range(3):
    print(current_thread().getName(),current_thread().ident,' is executing')
print('Printing list of threads')
for i in list_of_threads:
    print(i)

#Multi threading with out inheriting from Thread class
from threading import *
import time
def doubles(n):
   print(current_thread().getName())
   for i in n:
       time.sleep(1)
       print('Double of ',i,' is: ',2*i)
def squares(n):
   print(current_thread().getName())
   for i in n:
        time.sleep(1)
        print('Square of ',i,' is: ',i*i)
n=[2,4,6,8,10]
begintime=time.time()
t=Thread(target=doubles,args=(n,))
t1=Thread(target=squares,args=(n,))
t.start()
t1.start()
t.join()
t1.join()
current_thread().setName('Pawan Kalyan')
print(current_thread().getName())
endtime=time.time()
print('Total time taken is:',endtime-begintime)

#Multithreading without importing from Thread class
#using Thread(target=,args=)
from  threading import *
class MyThread:
    def display(self):
        for i in range(5):
            print(i,': executing')
my=MyThread()
t=Thread(target=my.display)
t.start()
for i in range(1,5):
    print('Hi uma')

#Multi Threading by importing from THread class
#not working
from threading import *
class MyThread(Thread):
    def display(self):
        print('hi')
        for i in range(2):
            print(i,' Good morning, Uma')
my=MyThread()
my.start()
print('Main Thread executing')
for i in range(5):
    print('Good Morning, Uma ',i)

# Multi Threading with out inheriting from Thread class


###########################################
from threading import *
import time
import datetime
def display():
    for i in range(5):
        print('Lazy thread',get_ident())
        time.sleep(2)
t=Thread(target=display)
t1=Thread(target=display)
#t.setDaemon(True)# if u make the thread t Daemon then output will be lazythread three times and main thread statement
t.start()
t1.start()
time.sleep(5)
print('Main thread exiting the program at:',datetime.datetime.now())
###########################################
from threading import *
def display(numbers):
    for i in numbers:
        print(i,' : Good morning, Uma')
numbers=[1,2,3,4,5]
t=Thread(target=display,args=(numbers,))
t.start()
for i in range(5):
    print('Good Morning, Uma :',i)
'''
