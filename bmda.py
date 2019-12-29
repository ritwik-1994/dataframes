import pandas as pd
df = pd.read_csv('/home/shipsy/Downloads/Pandas Part 1/bigmart_data.csv')
temp1 = df.sort_values(by =['Item_Outlet_Sales','Item_Weight'], ascending = False, inplace=True)
print(df[:5])
print(df.sort_index()[:5])
