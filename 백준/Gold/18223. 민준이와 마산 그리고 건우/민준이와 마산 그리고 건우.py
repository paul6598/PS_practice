import heapq
v,e,p = map(int,input().split())
graph = {}
for _ in range(e):
  a,b,c = map(int,input().split())
  if a in graph:
    graph[a][b] = c
  else:
    graph[a] = {b:c}
  if b in graph:
    graph[b][a] = c
  else:
    graph[b] = {a:c}


def dijk(graph, s,e):
  distance = [float('inf')]*(v+1)
  distance[s] = 0
  stack = []
  heapq.heappush(stack,(0,s))
  while stack:
    dist, node = heapq.heappop(stack)
    #print(dist, node)
    for next in graph[node]:
      if distance[next] > distance[node]+graph[node][next]:
        distance[next] = distance[node]+graph[node][next]
        heapq.heappush(stack,(graph[node][next],next))
  return distance[e]

if dijk(graph,1,v) == dijk(graph,1,p)+dijk(graph,p,v):
  print("SAVE HIM")
else:
  print("GOOD BYE")