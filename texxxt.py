import os
import sys
r = eval(input())
cj = [0 for i in range(r)]
for i in range(r):
  cj[i] = eval(input())
jg=0
yx=0
for i in range(r):
  if cj[i]>=60:
    jg+=1
  if cj[i]>=85:
    yx+=1
jgb = round(jg/r*100)
yxb = round(yx/r*100)
print("{}%".format(jgb))
print("{}%".format(yxb))

        
        

    

    
    
 
    
    
    
