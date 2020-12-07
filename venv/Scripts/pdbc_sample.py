'''
#updating table using dynamic values
#method II
import cx_Oracle
dsn_tns = cx_Oracle.makedsn('localhost', 1521, 'orcl')
con = cx_Oracle.connect('uma', 'uma', dsn_tns)
crsr=con.cursor()
increment=10000
sid=1
query1=f'update sample_pdbc1 set sal=sal+ {increment} where id = {sid}'
#query1='update sample_pdbc1 set sal=sal+ :increment where id = :sid'
#records=[(1000,1),(700,2),(900,3)]
#crsr.executemany(query1,records)

crsr.execute(query1)
con.commit()
crsr.close()
con.close()
#updating  table using dynamic values
#method I
import cx_Oracle
try:
    dsn_tns = cx_Oracle.makedsn('localhost', 1521, 'orcl')
    con = cx_Oracle.connect('uma', 'uma', dsn_tns)
    crsr=con.cursor()
    while True:
       query='update sample_pdbc1 set sal=sal+%f where id in %d'
       increment=float(input('Enter amount to increment:'))
       id_c= int(input('Enter id, whose sal you want to update:'))
       crsr.execute(query %(increment,id_c))
       option = input('Do you want to enter one more record:')
       if option == 'no':
           break
    con.commit()
except cx_Oracle.DatabaseError as e:
    print('Exception ',e,' occured')
    if con is None:
        con.rollback()
finally:
    if crsr is not None:
        crsr.close()
        con.close()

#inserting data into the table dynamically
import cx_Oracle
try:
    dsn_tns=cx_Oracle.makedsn('localhost',1521,'orcl')
    con=cx_Oracle.connect('uma','uma',dsn_tns)
    crsr=con.cursor()
    query='create table sample_pdbc1(name varchar2(20),id number(2),sal number(7,2))'
    crsr.execute(query)
    con.commit()
    crsr.close()
    crsr=con.cursor()
    query1='insert into sample_pdbc1 values(:name,:id,:sal)'
    records=[('uma',1,70000.00),
         ('vijay',2,80000.00),
         ('Adithya',3,90000.00)]
    crsr.executemany(query1,records)
    while True:
        query2="insert into sample_pdbc1 values('%s',%d,%f)"
        name=input('Enter name:')
        id=int(input('Enter id'))
        sal=float(input('Enter sal:'))
        crsr.execute(query2 %(name,id,sal))
        option=input('Do you want to enter one more record:')
        if option=='no':
            break
    con.commit()
except cx_Oracle.DatabaseError as e:
    print(con)
    if con:
        con.rollback()
        print('There is a problem ',e)
finally:
    if crsr:
        crsr.close()
        con.close()

#Selecting rows and displaying data using pandas
import datetime
import cx_Oracle
import pandas as pd
dsn_tns=cx_Oracle.makedsn('localhost',1521,'orcl')
con=cx_Oracle.connect('uma','uma',dsn_tns)
crsr=con.cursor()
print(con)
query=f'select * from emp'
crsr.execute(query)
row=pd.DataFrame(crsr.fetchall())
print(row)
print(row.shape)
#Same program with out pandas using list
import datetime
import cx_Oracle
dsn_tns=cx_Oracle.makedsn('localhost',1521,'orcl')
con=cx_Oracle.connect('uma','uma',dsn_tns)
crsr=con.cursor()
query=f'select * from emp'
crsr.execute(query)
row=crsr.fetchall()
for i in row:
    print(i)
crsr.close()
con.close()


# Program to select data from a table
import cx_Oracle
try:
    dsn_tns=cx_Oracle.makedsn('localhost',1521,service_name='orcl')
    con=cx_Oracle.connect(user='uma',password='uma',dsn=dsn_tns)
    crsr=con.cursor()
    crsr.execute('select * from songs')
    output=crsr.fetchone()
    print(output)
    for i in output:
        print(i)
except BaseException as msg:
    print('Connection is not successful ', msg)
finally:
    crsr.close()
    con.close()

#Program to insert records into the songs table

import cx_Oracle
try:
    dsn_tns=cx_Oracle.makedsn('localhost',1521,service_name='orsvcl')
    con=cx_Oracle.connect(user='uma',password='uma',dsn=dsn_tns)
    if con is not None:
        crsr=con.cursor()
        crsr.execute('insert into songs values(1,\'Buttabomma Buttabommma\',\'DeviSriPrasad\')')
        con.commit()
        print('1 Record inserted successfully')
    else:
        print('Can not connect to database')
except BaseException as msg:
    print('Connection is not successful ', msg)
#finally:
    #crsr.close()
    #con.close()


# Creating a table by connecting to oracle db using cx_Oracle module
import cx_Oracle
dsn_tns=cx_Oracle.makedsn('localhost',1521,'orcl')
con=cx_Oracle.connect(user=r'uma',password='uma',dsn=dsn_tns)
if con is not None:
    print('connection is successful')
else:
    print('Cant connect to oracle check the details provided')
crsr=con.cursor()
crsr.execute('CREATE TABLE songs(song_id NUMBER(2),title VARCHAR2(50),singer VARCHAR2(50))')
print('Table created successfully')
'''