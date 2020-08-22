d={'maths':100,'science':80,'social':58,'hindi':76,'telugu':86,'english':56}
print(d)
sum_of_values=sum(d.values())
print('Student score is: ',sum_of_values)

dnested={'student1':{'name':'uma','marks':[84,76,56,86,65,53]},
         'student2':{'name':'vijay','marks':[89,79,64,90,76,79]}
 }
for key,value in dnested.items():
    print('key: ',key,' value: ',value)

d_nested={'student1':'uma','marks_uma':{'maths':100,'science':80,'social':58,'hindi':76,'telugu':86,'english':56},
          'student2':'vijay','marks_vijay':{'maths':89,'science':76,'social':79,'hindi':79,'telugu':89,'english':64}
          }
for key,value in d_nested.items():
    print('key: ',key,' value: ',value)
print('value of marks vijay:',d_nested['marks_vijay']['english'])
