import sys
input = sys.stdin.readline

n = int(input())
nums = [0]
for _ in range(n):
  nums.append(nums[-1]+int(input()))
s,e = 0,0
smv = nums[-1]
res = 0

while e < n:
  tmp = nums[e]-nums[s]
  #print(tmp, smv-tmp)
  if tmp > smv-tmp:
    res = max(res, smv-tmp)
    s += 1
  elif tmp < smv-tmp:
    res = max(res, tmp)
    e += 1
  else:
    res = tmp
    break


print(res)