import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/home/shipsy/Downloads/Pandas Part 1/bigmart_data.csv')
df.dropna(how = 'any')
PLD = df[['Item_MRP','Item_Outlet_Sales']]
print(PLD.values[:5])
#x=PLD.index.tolist()
#y=PLD.values.tolist()
plt.title('Mean price for different items')
plt.xlabel('Sales')
plt.ylabel('MRP')
plt.scatter(df['Item_Outlet_Sales'][:50],df['Item_MRP'][:50],s=df['Item_Weight'][:50]*10)
plt.show()

