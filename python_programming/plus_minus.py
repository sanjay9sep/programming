import sys
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
length = float(len(arr))
pos=0
neg=0
zero=0

for i in arr:
    if i > 0:
       pos +=1
    elif i == 0:
         zero +=1
    else:
        neg +=1

print (pos/length)
print (neg/length)
print (zero/length)      
        
    
