n = int(input())
arr = list(map(int,input().split()))
ops = list(map(int,input().split()))
mxv = -float('inf')
mnv = float('inf')


def oper(a,b,c):
  if c == 0:
    return a+b
  elif c == 1:
    return a-b
  elif c == 2:
    return a*b
  else:
    if a > 0:
      return a//b
    else:
      return -(-a//b)

def back(ops,ret,index):
  global mxv, mnv
  #print(ret)
  if index == n:
    mxv = max(mxv,ret)
    mnv = min(mnv,ret)
  else:
    for i in range(4):
      if ops[i] > 0:
        ops[i] -= 1
        back(ops,oper(ret,arr[index],i),index+1)
        ops[i] += 1

back(ops,arr[0],1)
print(mxv)
print(mnv)