import sys
input = sys.stdin.readline

class UF():
  def __init__(self,n):
    self.parent = [i for i in range(n+1)]
    self.rank = [1]*(n+1)

  def find(self,x): #루트노드 반환
    if self.parent[x] == x:
      return x
    
    return self.find(self.parent[x])

  def union(self,x,y): 

    rootx = self.find(x)
    rooty = self.find(y)

    if rootx != rooty:
      if self.rank[rootx] > self.rank[rooty]:
        self.parent[rooty] = rootx
      elif self.rank[rootx] < self.rank[rooty]:
        self.parent[rootx] = rooty
      else:
        self.parent[rooty] = rootx
        self.rank[rootx] += 1


n,m = map(int,input().split())
uf = UF(n)

for _ in range(m):
  c,a,b = map(int, input().split())
  if c == 0:
    uf.union(a,b)
  else:
    if uf.find(a) == uf.find(b):
      print("YES")
    else:
      print("NO")