
n,m,k = map(int,input().split())
"""
dp[i][j]현재 위치가 i이고 j번 이동했을때 최댓값
"""

graph = {i:{} for i in range(1,n+1)} #도착지를 키값으로 


for _ in range(k):
  a,b,c = map(int,input().split())
  if a < b:
    if a in graph[b]:
      graph[b][a] = max(graph[b][a],c)
    else:
      graph[b][a] = c

#print(graph)
 
dp = [[0]*(m) for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1,m):
   for k in graph[i]:
    if (k != 1 and dp[k][j-1] != 0) or k == 1:
      dp[i][j] = max(dp[i][j],dp[k][j-1]+graph[i][k])
print(max(dp[-1]))