"""
an = a0+(n-1)*r

"""

def check(a1,n1,a2,n2):
  if (a2-a1)%(n2-n1) == 0:
    #r = (a2-a1)//(n2-n1)
    #a = a1-n1*r
    return [(a2-a1)//(n2-n1), a1-n1*((a2-a1)//(n2-n1))]
  return [float("inf"),float("inf")]

def sol(a,r,arr):
  cnt = 0
  for i in range(len(arr)):
    if arr[i] != i*r+a:
      cnt += 1
  return cnt


n = int(input())
arr = list(map(int, input().split()))
res = 500
for i in range(n):
  for j in range(i+1,n):
    r,a = check(arr[i],i,arr[j],j)
    #print(i,j,arr[i],arr[j],r,a)
    if r != float("inf"):
      res = min(res, sol(a,r,arr))
print(res)