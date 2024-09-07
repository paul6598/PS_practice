def fact(n,m=1):
  ret = 1
  for i in range(m+1,n+1):
    ret *= i
  return ret

def comb(n,m):
  return fact(n,m)//(fact(n-m))



n,m,k = list(map(int,input().split()))

if k != 0:
  y,x = k//m, k%m
  print(y,x)
  print(comb(y+x-1,y)*comb(m-x+n-y-1,n-y-1))
else:
  print(comb(n+m-2,m-1))