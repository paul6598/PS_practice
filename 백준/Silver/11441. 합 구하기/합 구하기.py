import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
acc = [0]
for i in nums:
  acc.append(acc[-1]+i)

m = int(input())
for _ in range(m):
  i,j = map(int,input().split())
  print(acc[j]-acc[i-1])