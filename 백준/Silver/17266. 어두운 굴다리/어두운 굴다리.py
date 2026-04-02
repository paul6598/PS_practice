import math
n = int(input())
m = int(input())
lights = list(map(int,input().split()))
mxv = max(1,lights[0], n-lights[-1])
for i in range(1,m):
  mxv = max(mxv, math.ceil((lights[i]-lights[i-1])/2))
print(mxv)