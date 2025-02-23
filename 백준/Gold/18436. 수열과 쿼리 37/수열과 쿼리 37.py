import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

tree = [0]*(4*n)
#홀수개수 세는 세그트리

def init(start=0,end=n-1,index=1):
  if start == end:
    tree[index] = 1 if arr[start] %2 == 1 else 0
    return tree[index]
  mid = (start+end)//2
  tree[index] = init(start,mid,2*index)+init(mid+1,end,2*index+1)
  return tree[index]


def query(left, right,start=0,end=n-1,index=1):
  if start > right or end < left:
    return 0
  if left <= start and end <= right:
    return tree[index]

  mid = (start+end)//2
  return query(left,right,start, mid, 2*index)+query(left,right,mid+1, end, 2*index+1)


def update(pos,diff,start=0,end=n-1,index=1):
  if pos < start or end < pos:
    return tree[index]

  if start == end:
    tree[index] = 1 if diff%2 == 1 else 0
    return tree[index]

  mid  = (start+end)//2
  tree[index] = update(pos,diff,start,mid,2*index)+update(pos,diff,mid+1,end,2*index+1)
  return tree[index]

init()

for _ in range(int(input())):
  a = list(map(int,input().split()))
  if a[0] == 1:
    update(a[1]-1, a[2])
    arr[a[1]-1] = a[2]
  elif a[0] == 2:
    print((a[2]-a[1]+1)-query(a[1]-1,a[2]-1))
  else:
    print(query(a[1]-1,a[2]-1))