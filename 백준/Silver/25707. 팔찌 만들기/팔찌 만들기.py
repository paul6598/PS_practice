n = int(input())
lis = list(map(int,input().split()))
lis.sort()

res = 0
for i in range(n):
  res += abs(lis[i-1]-lis[i])
print(res)