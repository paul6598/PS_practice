from collections import deque

n,m = map(int,input().split())
arr = []
for _ in range(n):
  arr.append(list(map(int,input().split())))

start = list(map(int,input().split()))
end = list(map(int,input().split()))
def bfs(start, end):
  dy, dx = [-1,0,1,0],[0,1,0,-1]
  visit = [[[float('inf')]*4 for _ in range(m)] for _ in range(n)]
  y,x,dir = start
  tmp = [0,2,4,3,1]
  visit[y-1][x-1][tmp[dir]-1] = 0
  end = [end[0]-1,end[1]-1,tmp[end[2]]-1]
  #visit[i][j][k] : i,j에서 k방향을 보고있을때 명령횟수
  q = deque([[y-1,x-1,tmp[dir]-1,0]])
  #print(end)
  while q:
    
    y,x,dir,com = q.popleft()
    #print(y,x,dir,com)
    if [y,x,dir] == end:
      return com
    if visit[y][x][(dir+1)%4] > com+1:
      q.append([y,x,(dir+1)%4,com+1])
      visit[y][x][(dir+1)%4] = com+1
    if visit[y][x][(dir-1)%4] > com+1:
      q.append([y,x,(dir-1)%4,com+1])
      visit[y][x][(dir-1)%4] = com+1
    for i in range(1,4):
      b,a = y+i*dy[dir],x+i*dx[dir]
      if 0<=b<n and 0<=a<m and visit[b][a][dir] > com+1:
        if arr[b][a] == 0:
          q.append([b,a,dir,com+1])
          visit[b][a][dir] = com+1
        else:
          break

print(bfs(start,end))