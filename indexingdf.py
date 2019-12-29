import pandas as pd
df = pd.read_csv("/home/shipsy/Downloads/Pandas Part 1/bigmart_data.csv")
print(df.sort_values(by="Outlet_Establishment_Year",ascending=False)[:10])
print(df.sort_values(by="Outlet_Establishment_Year")[:10])
df.sort_values(by="Outlet_Establishment_Year",ascending=False,inplace=True)
print(df.sort_values(by="Outlet_Establishment_Year")[:10])
