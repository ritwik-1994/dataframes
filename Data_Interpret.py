import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/home/shipsy/Downloads/Zajil-November.csv",nrows = 10000)
#print(df['reference_number'].value_counts())
#temp1 = df.pivot_table(values= 'reference_number', index='name', aggfunc= 'count')
#temp2 = pd.crosstab(index=df['name'],columns=df['name'])
#fig, ax = plt.subplots()
#df['name'].value_counts().plot(ax=ax, kind='bar')
#temp2= df['name'].value_counts().plot(kind='bar', stacked = True)
#plt.show()
#print(temp2)
#plt.show()	
#plt.show()
temp3 = pd.crosstab(df['name'], df['name'])
temp3.plot(kind='bar', stacked=True)
plt.show()

