import sys
input = sys.stdin.readline
"""
제일 가벼운 가방부터 순회하며 넣을 수 있는 보석들을 우선순위 큐에 삽입한다.
삽입이 끝나면 우선순위 큐에서 하나 뽑아 result에 더한다.
"""
import heapq

bags = []
jewl = []
n,k = map(int,input().split())
for _ in range(n):
  jewl.append(list(map(int,input().split())))

for _ in range(k):
  bags.append(int(input()))

bags.sort()
jewl.sort()
tmp = []
res = 0

for bag in bags:

  while jewl and jewl[0][0] <= bag:
    #print(jewl[0][0])
    heapq.heappush(tmp,-jewl[0][1])
    heapq.heappop(jewl)
  if tmp:
    res += -heapq.heappop(tmp)
  #print(jewl)    

print(res)