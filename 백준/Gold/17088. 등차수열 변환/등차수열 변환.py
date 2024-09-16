n = int(input())
nums = list(map(int,input().split()))

def sol(a,d,e):
  a += d
  for i in range(2,n):
    a += d
    if abs(nums[i]-a)>1:
      return float('inf')
    if nums[i] != a:
      e += 1
  return e


a = nums[0]
if n <= 2:
  print(0)
else:
  d = nums[1]-nums[0]
  k = [(a,d,0),(a,d+1,1),(a,d-1,1),
   (a-1,d+1,1),(a-1,d+2,2),(a-1,d,2),
    (a+1,d-1,1),(a+1,d-2,2),(a+1,d,2)]
  
  res = float('inf')
  for p,q,r in k:
    res = min(res,sol(p,q,r))
  if res == float('inf'):
    print(-1)
  else:
    print(res)