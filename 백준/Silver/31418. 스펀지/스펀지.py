import sys
input = sys.stdin.readline
"""
바이러스의 최대 영역을 서로 
"""
w,h,k,t = map(int,input().split())

def area(y,x):
  return (min(h-1,y+t)-max(0,y-t)+1)*(min(w-1,x+t)-max(0,x-t)+1)


res = 1
for _ in range(k):
  x,y = map(int,input().split())
  res *= area(y-1,x-1)
  res %= 998244353
print(res)