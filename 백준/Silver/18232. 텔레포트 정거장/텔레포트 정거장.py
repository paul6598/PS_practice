import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
s,e = map(int,input().split())

tele = {}
for _ in range(m):
  x,y = map(int,input().split())
  if x in tele:
    tele[x].append(y)
  else:
    tele[x] = [y]
  if y in tele:
    tele[y].append(x)
  else:
    tele[y] = [x]

visit = [0]*(n+1)
visit[s] = 0
q = deque([[s,0]])
while q:
  node, time = q.popleft()
  #print(node,time)
  if node == e:
    break
  if node+1 <= n and visit[node+1] == 0:
    visit[node+1] = 1
    q.append([node+1,time+1])
  if node-1 > 0 and visit[node-1] == 0:
    visit[node-1] = 1
    q.append([node-1,time+1])
  if node in tele:
    for next in tele[node]:
      if visit[next] == 0:
        visit[next] = 1
        q.append([next,time+1])

print(time)