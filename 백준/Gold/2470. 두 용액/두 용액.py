n = int(input())
sol = list(map(int,input().split()))
sol.sort()
s,e = 0,n-1
mxv = float('inf')
res = [0,0]
while s<e:
  mix = sol[s]+sol[e]
  if abs(mix) < mxv:
    mxv = abs(mix)
    res = [sol[s],sol[e]]
  if mix == 0:
    break
  elif mix < 0:
    s += 1
  else:
    e -= 1

print(*res)