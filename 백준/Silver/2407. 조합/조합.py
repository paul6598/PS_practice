def fac(n,m=1):
  ret = 1
  for i in range(m+1,n+1):
    ret *= i
  return ret

def sol(n,m):
  return fac(n,m)//fac(n-m)
n,m = map(int,input().split())
print(sol(n,m))