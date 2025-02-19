n,a,b = map(int,input().split())
mxv, mnv = max(a,b), min(a,b)

if mxv == 0:
  print(n)
elif mnv == 0:
  print(n//(mxv+1)+n%(mxv+1))
else:
  time = float("inf")
  cnt = 0
  while n >= 0:
    #print(n,mnv,sol(n,mnv,cnt))
    time = min(time, n//(mnv+1)+n%(mnv+1)+cnt)
    n -= mxv+1
    cnt += 1
    
  print(time)
