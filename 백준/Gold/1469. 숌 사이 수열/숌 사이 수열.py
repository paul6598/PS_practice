n = int(input())
arr = list(map(int,input().split()))
arr.sort()

dic = {i:2 for i in arr}
tmp = [-1]*17

tf = True

def back(arr,dic,tmp):
  global tf
  #print(*arr)
  if len(arr) == 2*n and tf:
    print(*arr)
    tf = False    
  for i in dic:
    if dic[i] == 2:
      for j in range(16):
        tmp[j] -= 1
      tmp[i] = i
      dic[i] -= 1
      back(arr+[i], dic,tmp)
      for j in range(16):
        tmp[j] += 1
      tmp[i] = -1
      dic[i] += 1

    elif dic[i] == 1 and tmp[i] == 0:
      for j in range(16):
        tmp[j] -= 1
      dic[i] -= 1
      back(arr+[i],dic,tmp)
      for j in range(16):
        tmp[j] += 1
      dic[i] += 1


back([],dic,tmp)
if tf:
  print(-1)