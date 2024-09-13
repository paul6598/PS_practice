n = int(input())
dp = [float('inf')]*(n+1)


def sol(n):
  return n*(n+1)*(n+2)//6

k = []
i = 1
while sol(i) <= n:
  k.append(sol(i))
  dp[sol(i)] = 1
  i += 1 


for i in range(1,n+1):
  for j in k:
    if j < i:
      dp[i] = min(dp[i-j]+1,dp[i])
      #print(dp)

print(dp[n])