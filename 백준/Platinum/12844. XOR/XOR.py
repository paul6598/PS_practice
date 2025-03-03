import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

tree = [0]*(4*n)
lazy = [0]*(4*n)

def init(index=1, start=0, end=n-1):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(2 * index, start, mid)^init(2 * index + 1, mid + 1, end)
    return tree[index]

def prop(index, start, end):
  if lazy[index] != 0:
    tree[index] = lazy[index]*((end-start+1)%2)^tree[index]
    if start != end:
      lazy[2*index] ^= lazy[index]
      lazy[2*index+1] ^= lazy[index]
    lazy[index] = 0

def update(left,right,value,index=1,start=0,end=n-1): #바뀐 합을 출력
  #print(left, right,start,end)
  prop(index, start, end)
  if right < start or end < left:
    return 0

  if left <= start and end <= right:
    tree[index] ^= value*((end-start+1)%2)
    if start != end:
      lazy[2*index] ^= value
      lazy[2*index+1] ^= value
    return tree[index]

  mid = (start+end)//2
  update(left, right, value, 2*index,start,mid)
  update(left, right, value, 2*index+1, mid+1, end)
  tree[index] = tree[2*index]^tree[2*index+1]
  return tree[index]



def query(left,right,index=1,start=0,end=n-1):
  prop(index, start, end)
  if right < start or end < left:
    return 0

  if left <= start and end <= right:
    return tree[index]

  mid = (start+end)//2
  return query(left,right,2*index,start,mid)^query(left,right,2*index+1,mid+1,end)



init()
#print(tree)
m = int(input())
for _ in range(m):
  o,*p = map(int,input().split())
  if o == 1:
    update(p[0],p[1],p[2])
    #print(tree)
  else:
    print(query(p[0],p[1]))
