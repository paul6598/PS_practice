n,m = map(int,input().split())
graph = [[float("inf")]*(n+1) for _ in range(n+1)]

for _ in range(m):
  u,v,t = map(int,input().split())
  graph[u][v] = t

k = int(input())
friends = list(map(int,input().split()))

for i in range(1,n+1):
  graph[i][i] = 0

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


res = float('inf')
index = []

for i in range(1,n+1):
  tmp = 0
  for friend in friends:
    tmp = max(tmp, graph[friend][i]+graph[i][friend])
  if tmp < res:
    res = tmp
    index = [i]
  elif tmp == res:
    index.append(i)

index.sort()
print(*index)

