
'''1 read employee table from sql serevr, practice database.
2)Retrive fields empid,empsalary,empname,empdepartment  from the employee dataframe
3)Derive salarystatus columnwith title high and low respectively for those whose salary is more than and less than average salary of all empoyees.
4)Fiter the emp details where department is 'CS'
5) join with address dataframe on the basis of id and then filter employe details who are from mumbai.
6) load the resultant dataframe in c drive local pc under EtlQn folder as resultant.tsv in tsv format  (tab seperated value).'''
import pandas as pd
import pandasql as ps
from conn import SqlConn


df=pd.read_sql('select * from [dbo].[EmployeeDetails]',SqlConn)

df= df.filter(items=['EmpId','Empsalary','Empdepartment','EmpName'])
df['avgsal']=df['Empsalary'].mean()

print(df)

def derivcol(Empsalary,avgsalaray):
    if Empsalary>avgsalaray:
        return 'high'
    elif Empsalary<avgsalaray:
        return 'low'
    
df['salarystatus']=df.apply(lambda r: derivcol(r['Empsalary'],r['avgsal']),axis=1)
df=df.drop(['avgsal'],axis=1)
df=df.loc[df['Empdepartment']=='CS']


df.to_csv('/EtlQn/pandasfunc.csv',index=False,mode='w',header=True)