n = int(input())
nums = list(map(int,input().split()))
snums = sorted(list(set(nums)))
res = [-1]*n
index = 0
sindex = 0

while index < n:
  for i in range(n):
    if snums[sindex] == nums[i] and res[i] == -1:
      res[i] = index
      index += 1
  sindex += 1

print(*res)