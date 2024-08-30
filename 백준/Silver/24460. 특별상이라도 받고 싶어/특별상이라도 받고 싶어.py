import sys
input = sys.stdin.readline

n = int(input())
table = []
for _ in range(n):
  table.append(list(map(int,input().split())))


def rcur(table,i,j,m):
  if m == 1:
    return table[i][j]
  ret = [rcur(table,i,j,m//2),rcur(table,i+m//2,j,m//2),rcur(table,i,j+m//2,m//2),rcur(table,i+m//2,j+m//2,m//2)]
  ret.sort()
  return ret[1]

print(rcur(table,0,0,n))