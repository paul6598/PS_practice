n = int(input())
k = n//2
dp = [1,1] #0,2,4,6
for i in range(2,k+1):
  tmp = 0
  if i%2 == 0:
    for j in range(i//2):
      tmp += dp[j]*dp[i-j-1]
      tmp %= 987654321
    tmp *= 2
    tmp %= 987654321
  else:
    for j in range(i//2):
      tmp += dp[j]*dp[i-j-1]
      tmp %= 987654321
    tmp *= 2
    tmp += dp[i//2]*dp[i//2]
    tmp %= 987654321
  dp.append(tmp)

print(dp[-1])