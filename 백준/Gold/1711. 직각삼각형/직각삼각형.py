import sys
input = sys.stdin.readline

n = int(input())
dots = []
for _ in range(n):
  dots.append(list(map(int,input().split())))

def dist(d1,d2):
  return (d1[0]-d2[0])**2+(d1[1]-d2[1])**2

def sol(d1,d2,d3): #d1 d2가 빗변
  if dist(d1,d2) == dist(d2,d3) + dist(d1,d3):
    return True
  else:
    return False

def solve(d1,d2,d3):
  if sol(d1,d2,d3) or sol(d1,d3,d2) or sol(d2,d3,d1):
    return True
  else:
    return False

res = 0

for i in range(n-2):
  for j in range(i+1,n-1):
    for k in range(j+1,n):
      if solve(dots[i],dots[j],dots[k]):
        res += 1
print(res)
