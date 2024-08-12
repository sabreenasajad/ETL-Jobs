import pandas as pd
import pandasql as ps
from conn import SqlConn
from sqlalchemy import create_engine, Integer, String, Float, Numeric
query1= "select * from [dbo].[EmployeeDetails]"
df1=pd.read_sql(query1,SqlConn)
print(df1)


df = pd.read_csv('/sourceFile/countries.csv',encoding='latin-1') 
df = ps.sqldf(""" select * from df where ISO_ALPHA2 like 'A%'""")
df = ps.sqldf(""" select *,(POPULATION + AREA_KM2) as Pop_Area from df """)
df = ps.sqldf(""" select  NAME,NATIONALITY,COUNTRY_CODE,ISO_ALPHA2,CAPITAL from df """)
# testing done
print(df.dtypes)

print(df)
#REGION_ID,Pop_Area
# Define the data types for each column
dtype = {
    'NAME': String(255),
    'NATIONALITY': String(255) ,
    'COUNTRY_CODE': String(255)  ,
    'ISO_ALPHA2': String(255)  ,
    'CAPITAL': String(255),  
    #'REGION_ID': Integer() ,
    #'Pop_Area':  Numeric(precision=10, scale=2) 
}
#,dtype =dtype
df.to_sql(name='popCountryD',schema='dbo', con=SqlConn,if_exists='replace',  index=False,dtype=dtype )

