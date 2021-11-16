import numpy as np
x=[40,10,20,5,45,50,65,90,35,25]
y=len(x)
z=x[:]
z.sort()
loc=[]
w=x[:]
w.sort(reverse=True)
v=x.count(x[0])
peak=[]
for i in range(y):
  if (v==y):
    print("v is used to check if all the elements are equal")
    peak.append(x[0])
    break
  if (z==x):                                                  
    print("z is the list to check ascending order condition")
    peak.append(z[-1])
    break
  if (w==x):
    print("w is the list to check descending order condition")
    peak.append(w[0])
    break
  if (x[i-1]<x[i] and x[i]>x[i+1]):
    peak.append(x[i])
    loc.append(i)
print("the peal values are:",peak)
print("the square root values of peak elements are: ",np.sqrt(peak))    

  