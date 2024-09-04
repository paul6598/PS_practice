#dp[i][j][k] : 길이가 i이고 비트수가 j이고 k로 끝나는 수열의 갯수

def sol(n,k):
  dp = [[[0,0] for _ in range(k+1)] for _ in range(n)]
  dp[0][0][0] = 1
  dp[0][0][1] = 1
  for i in range(1,n):
    for j in range(k+1):
      if j == 0:
        dp[i][j][1] = dp[i-1][j][0]
        dp[i][j][0] = dp[i-1][j][0]+dp[i-1][j][1]
      else:
        dp[i][j][1] = dp[i-1][j-1][1]+dp[i-1][j][0]
        dp[i][j][0] = dp[i-1][j][1]+dp[i-1][j][0]


  return sum(dp[-1][-1])

t = int(input())
for _ in range(t):
  n,k = map(int,input().split())
  print(sol(n,k))