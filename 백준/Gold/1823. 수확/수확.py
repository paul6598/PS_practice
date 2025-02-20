n = int(input())
q = [int(input()) for _ in range(n)]

# 초기 dp 배열 (인덱스 0부터 n+1까지)
dp0 = [0] * (n+2)  # 왼쪽에서 수확한 경우
dp1 = [0] * (n+2)  # 오른쪽에서 수확한 경우

for i in range(1, n+1):
    new_dp0 = [0] * (n+2)
    new_dp1 = [0] * (n+2)
    for j in range(1, n+1):
        if i >= j:  # 왼쪽(앞쪽) 벼를 수확하는 경우
            # dp0[i][j] = max(dp[i-1][j-1][0], dp[i-1][n-i+j+1][1]) + i*q[j-1]
            new_dp0[j] = max(dp0[j-1], dp1[n-i+j+1]) + i * q[j-1]
        if n+1-i <= j:  # 오른쪽(뒷쪽) 벼를 수확하는 경우
            # dp1[i][j] = max(dp[i-1][j+1][1], dp[i-1][i+j-n-1][0]) + i*q[j-1]
            new_dp1[j] = max(dp1[j+1], dp0[i+j-n-1]) + i * q[j-1]
    dp0, dp1 = new_dp0, new_dp1

# 결과: 마지막 단계(i = n)에서 j=1...n의 값들 중 최대값
result = max(max(dp0[1:n+1]), max(dp1[1:n+1]))
print(result)