import pandas as pd
import pandasql as ps
from conn import SqlConn
from sqlalchemy import create_engine, Integer, String, Float, Numeric

df = pd.read_csv('/sourceFile/countries.csv',encoding='latin-1') 
df = ps.sqldf(""" select * from df where ISO_ALPHA2 like 'A%'""")
df = ps.sqldf(""" select *,(POPULATION + AREA_KM2) as Pop_Area from df """)
df = ps.sqldf(""" select  NAME,NATIONALITY,COUNTRY_CODE,ISO_ALPHA2,CAPITAL,REGION_ID,Pop_Area from df """)
# testing done

# Define the data types for each column
dtype = {
    'NAME': String(255),
    'NATIONALITY': String(255) ,
    'COUNTRY_CODE': String(255) ,
    'ISO_ALPHA2': String(255) ,
    'CAPITAL': String(255) ,
    'REGION_ID': Float() ,
    'Pop_Area':  Float()
}

df.to_sql('dbo.popCountry', con=SqlConn, if_exists='replace', index=False,dtype =dtype )

