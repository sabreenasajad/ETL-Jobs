'''1)extract a csv file
2)find NAME,NATIONALITY,COUNTRY_CODE,ISO_ALPHA2,CAPITAL,POPULATION,AREA_KM2,REGION_ID
 whose area is below 10000 km, 
add an attribute 'Region' with values populated as below
if area is under 10k km then then populate with 'small'
if area is under 20k km then populate with ' medium'
else if area is under 50 k km then populate with ' high'
else if area is greater than 50 k km then populate with ' super high'
3) finally load the final file in D drive of local PC under etlqn folder.'''
import pandas as pd
import pandasql as ps 
df=pd.read_csv('/sourceFile/countries.csv',encoding='latin1')
#print(df)
df=ps.sqldf("""select NAME,NATIONALITY,COUNTRY_CODE,ISO_ALPHA2,CAPITAL,POPULATION,AREA_KM2,REGION_ID from df where
            AREA_KM2<10000""")
#print(df)
df=ps.sqldf("""select*,
            case
             when AREA_KM2<'10000'then 'small'
            when AREA_KM2<'20000'then 'medium'
            when AREA_KM2<'50000'then 'high'
             when AREA_KM2>'50000'then 'super high'

             end as region from df""")
print(df)
df.to_csv('/EtlQn/resultant2.csv',index=False)


