class UF():
  def __init__(self,n):
    self.parent = [i for i in range(n)]
    self.rank = [0 for _ in range(n)]

  def find(self,x):
    if self.parent[x] == x:
      return x
    return self.find(self.parent[x])

  def union(self,x,y):
    rx = self.find(x)
    ry = self.find(y)
    if rx == ry:
      return 
    if self.rank[rx] > self.rank[ry]:
      self.parent[ry] = rx
    elif self.rank[rx] < self.rank[ry]:
      self.parent[rx] = ry
    else:
      self.parent[ry] = rx
      self.rank[rx] += 1

n,m = map(int,input().split())
uf = UF(n)
t = 1
tf = True
for _ in range(m):
  a,b = map(int,input().split())
  if tf and uf.find(a) == uf.find(b):
    tf = False
    sol = t
  uf.union(a,b)
  t += 1

if tf:
  print(0)
else:
  print(sol)