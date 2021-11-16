import numpy as np
import pandas as pd
obj=[1,2,3,4,5,6,7]
profit=[10,5,15,7,6,18,3]
weight=[2,3,5,7,1,4,1]
pw=[]
cap=15
new=[]
x=[0,0,0,0,0,0,0]
for i in range(0,7):
  pw.append(profit[i]/weight[i])

new_list=list(pw)
for i in range(0,7):
  cap=cap-weight[new_list.index(np.max(new_list))]
  x[new_list.index(np.max(new_list))]=1
  new.append(cap)
  
  new_list[new_list.index(max(new_list))]=0
  if (cap<weight[new_list.index(np.max(new_list))]):
    cap=cap/weight[new_list.index(np.max(new_list))]
    new.append(cap)
    x[new_list.index(np.max(new_list))]=cap
    new_list[new_list.index(max(new_list))]=0
    break
print("KNAP SAC AFTER FILLING EACH OBJECT",new) 
print("THE GLOBAL ARRAY IS",x)
total_profit=[]
for i in range(0,7):
  y=x[i]*profit[i]
  total_profit.append(y)
print("The total profit is",sum(total_profit))