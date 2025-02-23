import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

tree = [0]*(4*n)
lazy = [0]*(4*n)

def init(start=0,end=n-1,index=1):
  if start == end:
    tree[index] = arr[start]
    return tree[index]
  mid = (start+end)//2
  tree[index] = init(start,mid,2*index)+init(mid+1,end,2*index+1)
  return tree[index]

def propa(start=0,end=n-1,index=1):
  if lazy[index] != 0:
    tree[index] += lazy[index]*(end-start+1)
    if start != end:
      lazy[2*index] += lazy[index]
      lazy[2*index+1] += lazy[index]
    lazy[index] = 0


def query(left, right,start=0,end=n-1,index=1):
  propa(start, end, index)
  if start > right or end < left:
    return 0
  if left <= start and end <= right:
    return tree[index]
  mid = (start+end)//2
  return query(left,right,start, mid, 2*index)+query(left,right,mid+1, end, 2*index+1)


def update(left, right,diff,start=0,end=n-1,index=1):
  propa(start, end, index)
  if right < start or end < left:
    return tree[index]

  if left <= start and end <= right:
    tree[index] += diff*(end-start+1)
    if start != end:
      lazy[2*index] += diff
      lazy[2*index+1] += diff
    return

  mid  = (start+end)//2
  update(left, right,diff,start,mid,2*index)
  update(left, right,diff,mid+1,end,2*index+1)


init()

for _ in range(int(input())):
  a = list(map(int,input().split()))
  if a[0] == 1:
    update(a[1]-1, a[2]-1,a[3])
  else:
    print(query(a[1]-1,a[1]-1))