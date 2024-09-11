import sys
input = sys.stdin.readline
_ = input()
nums = list(map(int,input().split()))
acc = [0]
for i in nums:
  acc.append(acc[-1]+i)
for _ in range(int(input())):
  i,j = map(int,input().split())
  print(acc[j]-acc[i-1])