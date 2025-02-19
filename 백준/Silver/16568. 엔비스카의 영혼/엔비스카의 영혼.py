def sol(n,m,cnt):
  if n <= m:
    return cnt+n
  res = 0
  res += n//(m+1)
  n %= m+1
  return res+n+cnt


n,a,b = map(int,input().split())
mxv, mnv = max(a,b), min(a,b)

if mxv == 0:
  print(n)
elif mnv == 0:
  if n == 0:
    print(0)
  else:
    print(sol(n,mxv,0))
else:
  time = float("inf")
  cnt = 0
  while n >= 0:
    #print(n,mnv,sol(n,mnv,cnt))
    time = min(time, sol(n,mnv,cnt))
    n -= mxv+1
    cnt += 1
    
  print(time)
