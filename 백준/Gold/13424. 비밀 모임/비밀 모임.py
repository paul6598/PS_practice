"""
플루이드 워셜
"""
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n,m = map(int,input().split())
  graph = {i:{} for i in range(1,n+1)}
  for _ in range(m):
    a,b,t = map(int,input().split())
    graph[a][b] = t
    graph[b][a] = t
  k = int(input())
  friend = list(map(int,input().split()))

  def floid(n,m,graph):
    dist = [[float('inf')]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
      dist[i][i] = 0

    for i in graph:
      for j in graph[i]:
        dist[i][j] = graph[i][j]

    for k in range(1,n+1):
      for i in range(1,n+1):
        for j in range(1,n+1):
          dist[i][j] = min(dist[i][k]+dist[k][j],dist[i][j])

    return dist

  res = floid(n,m,graph)

  mnv = float('inf')
  mnk = 0

  for i in range(1,n+1):
    tmp = 0
    for j in friend:
      tmp += res[i][j]

    if tmp < mnv:
      mnv = tmp
      mnk = i
    elif tmp == mnv:
      mnk = min(mnk,i)

  print(mnk)

