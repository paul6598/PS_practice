n = int(input())
table = []
for _ in range(n):
  table.append(list(map(int, input().split())))


res = float('inf')

dy = [0,0,1,-1]
dx = [1,-1,0,0]
for y1 in range(1,n-1):
  for x1 in range(1,n-1):
    for y2 in range(1,n-1):
      for x2 in range(1,n-1):
        for y3 in range(1,n-1):
          for x3 in range(1,n-1):
            if abs(y1-y2)+abs(x1-x2) > 2 and abs(y2-y3)+abs(x2-x3) > 2 and abs(y1-y3)+abs(x1-x3) > 2:
              tmp = table[y1][x1]+table[y2][x2]+table[y3][x3]
              for k in range(4):
                tmp += table[y1+dy[k]][x1+dx[k]]+table[y2+dy[k]][x2+dx[k]]+table[y3+dy[k]][x3+dx[k]]
              res = min(res,tmp)

print(res)