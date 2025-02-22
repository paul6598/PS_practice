import sys
input = sys.stdin.readline

n,q = map(int,input().split())
arr = [0]*n
tree = [0]*(4*n)

def update(pos,value,index=1,start=0,end=n-1):
  if pos < start or end < pos:
    return
  tree[index] += value
  if start == end:
    return
  mid = (start+end)//2
  update(pos,value,2*index,start,mid)
  update(pos,value,2*index+1,mid+1,end)

def query(left,right,index=1,start=0,end=n-1):
  if right < start or end < left:
    return 0
  if left <= start and end <= right:
    return tree[index]
  mid = (start+end)//2
  return query(left,right,2*index,start,mid)+query(left,right,2*index+1,mid+1,end)

for _ in range(q):
  k,i,j = map(int,input().split())
  if k == 1:
    diff = j - arr[i-1]  # 값 차이 계산
    arr[i-1] = j  # 배열 업데이트
    update(i-1, diff)
  else:
    print(query(min(i-1,j-1),max(i-1,j-1)))