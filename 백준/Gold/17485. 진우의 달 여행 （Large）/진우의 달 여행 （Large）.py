n,m = map(int,input().split())
table = []
for _ in range(n):
    table.append(list(map(int,input().split())))

dp = [[[float('inf')]*m for _ in range(n)] for _ in range(3)]
dp[0][0] = table[0]
dp[1][0] = table[0]
dp[2][0] = table[0]


for i in range(1,n):
  for j in range(m):
    if j != m-1:
      dp[0][i][j] = min(dp[1][i-1][j+1],dp[2][i-1][j+1])+table[i][j]
    dp[1][i][j] = min(dp[0][i-1][j],dp[2][i-1][j])+table[i][j]
    if j != 0:
      dp[2][i][j] = min(dp[0][i-1][j-1],dp[1][i-1][j-1])+table[i][j]

print(min(dp[0][n-1]+dp[1][n-1]+dp[2][n-1]))
#print(dp)