from collections import deque

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
tf = False

for i in range(n):
  if tf:
    break
  for j in range(m):
    if arr[i][j] == 2:
      sy, sx = i,j
      tf = True
      break
  
def bfs():
  visit = [[-1]*m for _ in range(n)]
  q = deque([[sy,sx,0]])
  visit[sy][sx] = 0
  dy,dx = [0,0,1,-1],[1,-1,0,0]
  while q:
    b,a,move = q.popleft()
    for i in range(4):
      y,x = b+dy[i],a+dx[i]
      if 0<=y<n and 0<=x<m and visit[y][x] == -1 and arr[y][x] == 1:
        visit[y][x] = move+1
        q.append([y,x,move+1])
  return visit

visit = bfs()
for i in range(n):
  for j in range(m):
    if arr[i][j] == 0:
      print(0, end = " ")
    else:
      print(visit[i][j], end = " ")
  print()