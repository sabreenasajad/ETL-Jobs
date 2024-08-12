
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
#print(df)
df=ps.sqldf("""select*,
            case
             when Empsalary > (select avg(Empsalary) from df) then 'High'
             when Empsalary < (select avg(Empsalary) from df) then 'low'
            ELse 
            'Empsalary' End as salarystatus from df""")
#print(df)
df=ps.sqldf("""select * from df where Empdepartment='CS'""")
#print(df)


df1=pd.read_sql('select * from [dbo].[AddressDetails]',SqlConn)
#print(df1)
df=ps.sqldf(""" select e.* from df e inner join df1 a on e.Empid=a.id where a.state ='mumbai'""")  
#print(df2)
df.to_csv('/EtlQn/resultant.tsv',sep='|',index=False,mode='w',header=False)




