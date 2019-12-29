import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
#import warnings as warn

#warn.filterwarnings("ignore")
df =pd.read_csv('/home/shipsy/Downloads/Pandas Part 1/bigmart_data.csv')
print(df.head())
plt.plot(df['Item_MRP'])
plt.show()
