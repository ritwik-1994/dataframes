import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

height = [1,2,3,4]
weight = [8,7,6,5]

#plt.plot(height,weight)
#plt.title("Relationship between height and weight")
#plt.xlabel("Height")
#plt.ylabel("Weight")
#plt.show()
#plt.figure(figsize=(5,5))
Calories_Burnt = [65,75,99,107] 
#plt.plot(Calories_Burnt,'m--')
#plt.plot(weight, 'ro')
#plt.legend(labels=["Calories_Burnt","Weight"], loc ='middle right')
#plt.xticks((0,1,2,3), ('p1','p2','p3','p4'))
#plt.show()


fig, ax = plt.subplots(nrows=1,ncols=2, figsize=(5,5), sharey=True)

ax[0].plot(Calories_Burnt, 'ro')
ax[0].set_title("Calories_Burnt")
ax[0].set_xlabel("Person")
ax[0].set_ylabel("Calories Burnt")
ax[0].set_xticks((0,1,2,3))
ax[0].set_xticklabels(('p1','p2','p3','p4'))
ax[1].plot(weight)
plt.show()
