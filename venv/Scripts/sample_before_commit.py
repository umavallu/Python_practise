#USER DEFINED MODULE
#This module is saved in the file detaila_module.py
name='uma'
husband='vijay'
child1,child2='adithya','pradyumna'
def parents(name):
    if name.upper()=='UMA':
            parents='Koteswararao and Ramadevi'
    else:
            parents='This persons parents records are not available'
    return parents
def printing(name):
    if name.upper()=='UMA':
        print('printing your name:', name)
    return name
''''Using the above user defined module in another python file'''
#All the below python files use the above module in different scenarios

#METHOD1
from details_module import name,husband,child1,child2
def print_details():
    print('Your name is:',name)
    print('Your name is:',husband)
    print('Your name is:',child1)
    print('Your name is:',child2)
    #print('Your name is:',parents)
print_details()
#METHOD2
from details_module import *
def print_details():
    print('Your name is:',name)
    print('Your name is:',husband)
    print('Your name is:',child1)
    print('Your name is:',child2)
    #print('Your name is:',parents)
print_details()
#method3
import details_module as dm
def print_details():
    print('Your name is:',dm.name)
    print('Your name is:',dm.husband)
    print('Your name is:',dm.child1)
    print('Your name is:',dm.child2)
    print('Your name is:',parents)
print_details()
#method4 sleep(15) and reload()

import details_module as dm
import time
def print_details():
    print('Your name is:',dm.name)
    print('Your name is:',dm.husband)
    print('Your name is:',dm.child1)
    print('Your name is:',dm.child2)
    print('Your parents are:',dm.parents('uma'))
    print('Program is entering into sleeping state')
    time.sleep(45)
    dm.printing('uma')
    print('Program is waking up')
print_details()