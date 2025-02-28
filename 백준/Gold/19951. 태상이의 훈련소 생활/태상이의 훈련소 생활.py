import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))


tree = [0]*(4*n)
lazy = [0]*(4*n)
def init(index=1, start=0, end=n-1):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(2 * index, start, mid) + init(2 * index + 1, mid + 1, end)
    return tree[index]

def prop(index=1, start=0, end=n-1):
  if lazy[index] != 0:
    tree[index] += lazy[index]* (end - start + 1)
    if start != end:
      lazy[2*index] += lazy[index]
      lazy[2*index+1] += lazy[index]
    lazy[index] = 0

def update(left, right, diff, index=1, start=0, end=n-1):
  prop(index,start,end)
  if end < left or right < start:
    return
  if left <= start and end <= right:
    tree[index] += diff*(end-start+1)

    if start != end:
      lazy[2*index] += diff
      lazy[2*index+1] += diff
    return

  mid = (start+end)//2
  update(left, right, diff, 2*index, start, mid)
  update(left, right, diff, 2*index+1, mid+1, end)

  tree[index] = tree[2*index]+tree[2*index+1]

def query(left, right, index=1, start=0, end=n-1):
    prop(index, start, end) 

    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return tree[index]

    mid = (start + end) // 2
    return query(left, right, 2 * index, start, mid) + query(left, right, 2 * index + 1, mid + 1, end)

init()
for i in range(m):
  a,b,k = map(int,input().split())
  update(a-1,b-1,k)

for i in range(n):
  print(query(i,i), end = " ")