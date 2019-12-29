import pandas as pd
import numpy as n
##read CSV
df = pd.read_csv('/home/shipsy/Downloads/Pandas Part 1/bigmart_data.csv')
##drop null values
#df.dropna(how='any')
##reset inde after drop values
#df.reset_index(drop=True)
##read top rows
#print(df.head())	

#Aggregating Data
#Group By

#print(df.groupby(['Item_Type','Item_Fat_Content']).mean())
#print(pd.crosstab(df['Outlet_Size'],df['Outlet_Location_Type'],margins=True))
print(df.pivot_table(index = ['Outlet_Establishment_Year','Item_Type'], values = 'Item_Outlet_Sales', aggfunc = [n.mean, n.median, min, max, n.std]))
