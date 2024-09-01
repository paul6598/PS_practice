"""
  2 2 3  4  9 10
0 2 4 7 11 20 30
(nums[i]*i-asum[i])+(asum[-1]-asum[i]-nums[i]*(n-i)
nums[i]*(2*i-n)-2*asum[i]+asum[-1]
"""

n = int(input())
town = {}
for _ in range(n):
  x,a = map(int, input().split())
  town[x] = a

town = dict(sorted(town.items(), key=lambda item: item[0]))
people = sum(town.values())
res = 0

if people%2 == 0:
  for i in town:
    res += town[i]
    if res >= people//2:
      print(i)
      break
else:
  for i in town:
    res += town[i]
    if res > people//2:
      print(i)
      break
