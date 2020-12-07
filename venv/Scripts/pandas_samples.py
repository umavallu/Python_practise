import pandas as pd
import cx_Oracle
import logging
import datetime
dsn_tns=cx_Oracle.makedsn('localhost',1521,'orcl')
con=cx_Oracle.connect('uma','uma',dsn_tns)
crsr=con.cursor()
crsr.execute('select * from emp')
logging.basicConfig(filename='C:/Users/Vijay/PycharmProjects/untitled/venv/logging_text.txt',level=logging.WARNING,)
#logging.warning('Selecting data from Employee table')
#logging.warning(datetime.datetime.now())
emp_df=pd.DataFrame(crsr.fetchall())
print(emp_df)
crsr.close()
con.close()
print(emp_df.columns)
logging.warning(emp_df)
logging.warning(emp_df.columns)
print(emp_df.shape)
print(emp_df.info())
print(emp_df.head())
print(emp_df.tail())
print(emp_df.loc[[0,3],[1]])
print(emp_df.loc[3])
print(emp_df.iloc[5])
print(emp_df.iloc[[2,3],5])
print(emp_df.loc[[0,1]])
print(emp_df.loc[[0,1],[1,2]])
print(emp_df[1])
print(emp_df.shape)
print(emp_df[7].value_counts())
print(emp_df.loc[[1],[7]])
print(emp_df.loc[1,7])
print(emp_df.loc[[0,1,2],7])
print(emp_df.loc[0:2,3])
print(emp_df.iloc[0:2,0:4])
'''
#Pandas
#Converting dictionary to DataFrame and Analysis
import pandas as pd
print("Creating a dictionary")
d={'name':['Uma','Vijay','Adithya','Pradyu'],
   'lname':['maheswari','kumar','nath','mna'],
   'email':['umam@gmail.com','vijayk@gmail.com','adithyat@gmail.com','pradyumna@gmail.com']}
print('dictionary :',d)
df=pd.DataFrame(d)
print(df)
print(df['name'])
print(df.name)
print(df.shape)
print(df.info())
print(type(df.name))
print(df[['name','lname']])#to access a list of series of a dataframe
print(df.name,df.lname)
print(df.columns)#lists all columns in dataframe
print(df.iloc[2])#accessing row using index
#Pandas data Analysis
import pandas as pd
fpd=pd.read_csv('C:/Users/Vijay/Documents/MyFamily.csv')
print(fpd)
print(fpd.shape)
print(fpd.info())
pd.set_option('display.max_rows',10)
print(fpd)
print(fpd.head())
print(fpd.tail())
'''