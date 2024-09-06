def fac(n):
  ret = 1
  for i in range(1,n+1):
    ret *= i
  return ret

def sol(n,m):
  return fac(n)//(fac(m)*fac(n-m))
n,m = map(int,input().split())
print(sol(n,m))