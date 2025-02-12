n,m,k = map(int,input().split())
res = [i for i in range(1,k)]
res.extend([i for i in range(n,m,-1)])
res.extend([i for i in range(k,m+1)])

if m+1 <= n:
  print(*res)
else:
  print(-1)