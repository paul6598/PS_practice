n = int(input())
nums = list(map(int,input().split()))
dp = [0]*n
for i in range(n):
  mxv = 0
  for j in range(i):
    if nums[i] > nums[j]:
      mxv = max(mxv,dp[j])
  dp[i] = mxv+1
  #print(dp)

print(max(dp))