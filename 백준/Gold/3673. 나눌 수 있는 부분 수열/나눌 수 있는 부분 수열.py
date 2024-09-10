import sys
input = sys.stdin.readline
from collections import defaultdict

def sol(m,nums):
  ret = 0
  acc = [0]
  dic = defaultdict(int)
  for i in nums:
    dic[acc[-1]] += 1
    acc.append((acc[-1]+i)%m)
  dic[acc[-1]] += 1
  for i in dic:
    ret += (dic[i]*(dic[i]-1))//2
  return ret

c = int(input())
for _ in range(c):
  d,n = map(int,input().split())
  lis = list(map(int,input().split()))
  print(sol(d,lis))