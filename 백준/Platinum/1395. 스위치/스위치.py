n,m = map(int,input().split())

tree = [0]*(4*n)
lazy = [0]*(4*n)

def update(left,right,index=1,start=1,end=n): #바뀐 합을 출력
  if lazy[index]%2 == 1:
    tree[index] = end-start+1 - tree[index]
    if start != end:
      lazy[2*index] += 1
      lazy[2*index+1] += 1
    lazy[index] = 0
  if right < start or end < left:
    return

  
  if left <= start and end <= right:
    tree[index] = end-start+1 - tree[index]
    if start != end:
      lazy[2*index] += 1
      lazy[2*index+1] += 1
    return 


  mid = (start+end)//2
  update(left,right,2*index,start,mid)
  update(left,right,2*index+1,mid+1,end)
  tree[index] = tree[2*index]+tree[2*index+1]



def query(left,right,index=1,start=1,end=n):
  if lazy[index]%2 == 1:
    tree[index] = end-start+1 - tree[index]
    if start != end:
      lazy[2*index] += 1
      lazy[2*index+1] += 1
    lazy[index] = 0

  if right < start or end < left:
    return 0

  if left <= start and end <= right:
    return tree[index]

  mid = (start+end)//2
  return query(left,right,2*index,start,mid)+query(left,right,2*index+1,mid+1,end)

for _ in range(m):
  o,s,t = map(int,input().split())
  if o == 0:
    update(s,t)

  else:
    print(query(s,t))
