import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tree = [[0,0] for _ in range(4*n)]
arr = [int(input()) for _ in range(n)]

def init(index=1,start=0,end=n-1):

  if start == end:
    #print(arr[start])
    tree[index][0] = arr[start]
    tree[index][1] = arr[start]
    return tree[index]
  mid = (start+end)//2
  front, back = init(2*index,start,mid), init(2*index+1,mid+1,end)
  tree[index] = [max(front[0], back[0]), min(front[1], back[1])]
  return tree[index]

def query(left,right,index=1,start=0,end=n-1):
  if right < start or end < left:
    return [-float("inf"),float("inf")]
  if left <= start and end <= right:
    return tree[index]
  mid = (start+end)//2
  front, back = query(left,right,2*index,start,mid), query(left,right,2*index+1,mid+1,end)
  return [max(front[0], back[0]), min(front[1], back[1])]

init()

for _ in range(m):
  a,b = map(int,input().split())
  tmp = query(a-1, b-1)
  print(tmp[1], tmp[0])