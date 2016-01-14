import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)
l=len(a)
sum=0
sum1=0
for j in xrange(l):
    sum += a[j][j]
    sum1 += a[j][l-1-j]
diff = sum - sum1
print abs(diff)
    

