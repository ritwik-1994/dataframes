import numpy as np
x = np.arange(2,40,8)
condlist = [x<7 , (x>=10) & (x<20), x>22 ]
choicelist= ["equal to", "squared", "cubed"]
print(np.select(condlist, choicelist))	
 
