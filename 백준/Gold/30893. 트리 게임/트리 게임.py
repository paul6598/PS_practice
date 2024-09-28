import sys
input = sys.stdin.readline
from collections import deque
n,s,e = map(int,input().split())
tree = {i:[] for i in range(1,n+1)}
for i in range(n-1):
  u,v = map(int,input().split())
  tree[u].append(v)
  tree[v].append(u)

def bfs(tree,s,e):
  visit = [0]*(n+1)
  visit[s] = 1
  q = deque([[s,0,True]])
  while q:
    node, dist, tf = q.popleft()
    if node == e:
      return tf
    for next in tree[node]:
      if visit[next] == 0:
        if dist%2 == 1 and len(tree[node]) > 2:
          visit[next] = 1
          q.append([next,dist+1,False])
        else:
          visit[next] = 1
          q.append([next,dist+1,tf])          

if bfs(tree,s,e):
  print("First")
else:
  print("Second")