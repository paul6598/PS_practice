import sys
input = sys.stdin.readline

na,nb = map(int,input().split())

tf = False
m = int(input())
for _ in range(m):
  u,v = map(int,input().split())
  if u%2 == 1 and v%2 == 1:
    tf = True

if na%2 == 1 and nb%2 == 1:
  if tf:
    print(na//2+nb//2+1)
  else:
    print(na//2+nb//2)
else:
  print(na//2+nb//2)