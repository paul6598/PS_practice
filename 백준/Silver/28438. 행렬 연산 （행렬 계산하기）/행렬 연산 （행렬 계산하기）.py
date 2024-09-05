import sys
input = sys.stdin.readline
"""
c 리스트 r 리스트
[0]*n
[0]*m
"""

n,m,q = map(int,input().split())
r,c = [0]*n, [0]*m

for _ in range(q):
  a,u,v = map(int,input().split())
  if a == 1:
    r[u-1] += v
  else:
    c[u-1] += v

for i in range(n):
  for j in range(m):
    print(r[i]+c[j], end=" ")
  print()