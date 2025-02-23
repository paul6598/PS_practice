import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

tree = [0]*(4*len(arr))

def init(start=0,end=n-1,index=1):
  if start == end:
    tree[index] = arr[start]
    return tree[index]
  mid = (start+end)//2
  tree[index] = min(init(start,mid,2*index),init(mid+1,end,2*index+1))
  return tree[index]


def query(left, right,start=0,end=n-1,index=1):
  if start > right or end < left:
    return float("inf")
  if left <= start and end <= right:
    return tree[index]
  mid = (start+end)//2
  return min(query(left,right,start, mid, 2*index),query(left,right,mid+1, end, 2*index+1))


def update(pos,diff,start=0,end=n-1,index=1):
  if pos < start or end < pos:
    return tree[index]
  
  if start == end:
    tree[index] = diff
    return tree[index]
  mid  = (start+end)//2
  tree[index] = min(update(pos,diff,start,mid,2*index),update(pos,diff,mid+1,end,2*index+1))
  return tree[index]

init()

for _ in range(int(input())):
  a,b,c = map(int,input().split())
  if a == 1:
    update(b-1,c)
    arr[b-1] = c
  else:
    print(query(b-1,c-1))