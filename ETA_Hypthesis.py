import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/home/shipsy/Downloads/ETA_Actual_Data.csv')
DPI67247 = df[df['store_id']=='DPI67247']
DPI67247 = DPI67247.reset_index()
#DPI65926['difference'] = [DPI65926['Actual Delvery Time'] - DPI65926['Google ETA']]
temp_diff = []
plt.figure(figsize=(150,150))
for i in range(len(DPI67247)):
	temp_diff.append(round(DPI67247['Actual Delvery Time'][i]-DPI67247['Google ETA'][i],2))
DPI67247['difference'] = temp_diff	
#f = open('/home/shipsy/Downloads/DPI65926_describe.CSV','w+')
#DPI67247.describe().to_csv('/home/shipsy/Downloads/DPI65926/DPI67247_describe.CSV')
print(DPI67247.describe())
DPI67247[:1500].plot(kind='hist', color = 'r')
plt.xlabel('Order Index : DPI67247')
plt.ylabel('Actual Delivery Time - Google ETA')
#plt.xticks((0,150,300,450,600,750,900,1050,1200,1350,1500), ('0','370','740','1110','1480','1850','2220','2590','2960','3330','3775'))
plt.show()
#DPI65926['difference'][500:1000].plot(kind='line')
#plt.show()
#print(DPI65926.describe())
#exceptions = {}

#for i in range(len(DPI65926)):
#	if(DPI65926['
#	exceptions{}

