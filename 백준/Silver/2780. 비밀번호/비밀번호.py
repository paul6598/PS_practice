

dp = [[1,1,1,1,1,1,1,1,1,1]]
for _ in range(999):
  tmp = [dp[-1][7],dp[-1][2]+dp[-1][4],dp[-1][1]+dp[-1][3]+dp[-1][5],
            dp[-1][2]+dp[-1][6],dp[-1][1]+dp[-1][5]+dp[-1][7],
        dp[-1][2]+dp[-1][4]+dp[-1][6]+dp[-1][8],dp[-1][3]+dp[-1][5]+dp[-1][9]
            ,dp[-1][4]+dp[-1][8]+dp[-1][0],
        dp[-1][5]+dp[-1][7]+dp[-1][9],dp[-1][6]+dp[-1][8]]
  dp.append(tmp)
  for i in range(10):
    dp[-1][i] %= 1234567


t = int(input())
for _ in range(t):
  n = int(input())
  print(sum(dp[n-1])%1234567)