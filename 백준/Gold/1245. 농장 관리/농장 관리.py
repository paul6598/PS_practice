from collections import deque
"""
이중반복문으로 돌면서
방문한적 없고, 같은 숫자를 bfs. 
bfs중에 인접한 칸에 더 큰 숫자가 없었으면 res += 1
"""

n,m = map(int,input().split())

table = []
for _ in range(n):
  table.append(list(map(int, input().split())))

dy = [-1,1,0,0,1,1,-1,-1]
dx = [0,0,-1,1,-1,1,1,-1]

res = 0
visit = [[0]*m for _ in range(n)]


def bfs(y,x,h):
  tf = True
  q = deque([(y,x,h)])
  visit[y][x] = 1
  while q:
    i,j,height = q.popleft()
    for k in range(8):
      ny,nx = i+dy[k],j+dx[k]
      if 0<=ny<n and 0<=nx<m:
        if table[ny][nx] == height  and visit[ny][nx] == 0:
          visit[ny][nx] = 1
          q.append((ny,nx,table[ny][nx]))
        elif table[ny][nx] > height:
          tf = False
  return tf

for i in range(n):
  for j in range(m):
    if visit[i][j] == 0:
      if bfs(i,j,table[i][j]):
        res += 1

print(res)