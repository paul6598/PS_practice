n,m = map(int, input().split())
table = [[0]*m for _ in range(n)]

for i in range(3):
  tmp = list(map(int, input().split()))
  k = tmp[0]
  for j in range(k):
    table[tmp[2*j+1]-1][tmp[2*j+2]-1] = i+1



#q:1, k:2, p:3

def put_queen(y,x,table):
  dy,dx = [1,1,1,0,-1,-1,-1,0],[-1,0,1,1,1,0,-1,-1]
  for k in range(8):
    i,j = y+dy[k],x+dx[k]
    while 0<=i<n and 0<=j<m :
      #print(i,j)
      if table[i][j]==0 or table[i][j]==-1:
        table[i][j] = -1
      else:
        break
      i,j = i+dy[k],j+dx[k]


def put_knight(y,x,table):
  dy,dx = [1,2,2,1,-1,-2,-2,-1],[2,1,-1,-2,-2,-1,1,2]
  for k in range(8):
    ny,nx = y+dy[k],x+dx[k]
    if 0<=ny<n and 0<=nx<m and table[ny][nx]==0:
      table[ny][nx] = -1

for i in range(n):
  for j in range(m):
    if table[i][j]==1:
      put_queen(i,j,table)

    elif table[i][j]==2:
      put_knight(i,j,table)




res = 0
for i in range(n):
  for j in range(m):
    if table[i][j]==0:
      res+=1
print(res)