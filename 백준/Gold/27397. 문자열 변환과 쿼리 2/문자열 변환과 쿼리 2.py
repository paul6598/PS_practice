arr, n = input().split()
n = int(n)

def two(arr):
  ret = 1
  tmp = 1
  for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
      tmp += 1
    else:
      ret = max(ret,tmp)
      tmp = 1
  ret = max(ret,tmp)
  return ret

for _ in range(n):
  tmp = list(input().split())
  if len(tmp) == 1:
    print(two(arr))
  else:
    arr = arr.replace(tmp[1],tmp[2])
