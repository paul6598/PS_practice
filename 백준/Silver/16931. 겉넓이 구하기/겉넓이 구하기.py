n,m = map(int,input().split())
table = [[0]*(m+2) for _ in range(n+2)]
for i in range(1,n+1):
  table[i][1:m+1] = list(map(int,input().split()))

res = 2*n*m
for i in range(n+1):
  for j in range(m+1):
    res += abs(table[i][j]-table[i][j+1])
    res += abs(table[i][j]-table[i+1][j])


print(res)