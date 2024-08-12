import pandas as pd

df = pd.read_csv('/sourceFile/countries.csv',encoding='latin-1') 
print(df)
#df =df.loc[1:3,['NAME','NATIONALITY','COUNTRY_ID']]
#df=df.iloc[2]

df=df.filter(items=['SUB_REGION_ID','COUNTRY_ID','NAME']).sort_values(by=['SUB_REGION_ID','COUNTRY_ID'],ascending=True)
df=df.groupby("SUB_REGION_ID").agg({'COUNTRY_ID':['sum','min','max']})
print(df)