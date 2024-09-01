"""
dp[i][j] = 자릿수가 i이고, 자릿수의합을 3으로 나눈 나머지가 j
"""


n = int(input())

dp = [[0]*3 for _ in range(n)] 
dp[0][0],dp[0][1],dp[0][2] = 0,1,1
for i in range(1,n):
  for j in range(3):
    dp[i][j] = sum(dp[i-1])%1000000009

print(dp[n-1][0])

  
