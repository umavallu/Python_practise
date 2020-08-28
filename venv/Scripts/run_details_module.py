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