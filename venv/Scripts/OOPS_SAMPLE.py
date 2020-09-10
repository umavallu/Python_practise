'''
class Family:
    def __init__(self):
        self.father='Vijay'
        self.mother='Uma'
        self.elder_son='Adithya'
        self.younger_son='Pradyumna'
    def print_family(self):
        print('Welcome')
        print('Father: '+self.father)
        print('Mother: '+self.mother)
        print('First child: '+self.elder_son)
        print("second child: "+self.younger_son)
f=family()
f.print_family()
------------------------------------------------------
class Student:
    def __init__(self,name,grade,age,school):
        self.name=name
        self.grade=grade
        self.age=age
        self.school=school
    def child_details(self):
        print('student name: '+self.name)
        print('student grade: '+self.grade)
        print('seudent age: ',self.age)
        print('student school:'+self.school)
s=student('Adithya','five',10,'Broadmoor')
s.child_details()
s=student('Pradyumna','pre-k3',4,'Fishers')
s.child_details()
s.__init__('vijay','pg',35,'university of ')
s.child_details()
--------------------------------------------------
def sample_m():
    print('Hi,sample method')
class Sample:
    a='uma'
    b=4
    def __init__(self):
        print('Constructor is executing')
    def __init__(self,a):
        a='maheswari'
        print(a)
    def sample_m(self):
        print('sample function')
    print('a= ',a)
    print('b= ',b)
s=Sample(9)
sample_m()
s.sample_m()
s=Sample('uma')
'''
students=[]
class Student:
    university="KLU" #static variable
    def __init__(self): #s_name,s_course,s_duration are instance variables
        self.s_name=input('Enter student name: ')
        self.s_course=input('Enter student course: ')
        self.s_duration=input('Enter duration of course: ')
    def student_info(self):
        print('Student: ',self.s_name)
        print('Course: ',self.s_course)
        print('s_duration: ',self.s_duration)

while True:
    option = input('Do you want to enter student record:(yes/no) ')
    if option.lower() == 'no':
        break
    else:
        s=Student()
        students.append(s)
        print('Student record entered successfully')

choice=input('Do you want to see student information (yes/no):')
if choice.upper()=='YES':
    print('Students records')
    for i in students:
        print(i.student_info())
