def minmin(arr):
  res = ""
  prev_m = False
  for i in range(len(arr)):
    if arr[i] == "K":
      res += "5"
    else:
      if prev_m:
        res += "0"
      else:
        res += "1"
    if arr[i] == "M":
      prev_m = True
    else:
      prev_m = False
  return int(res)

def minmax(arr):
  last_k = -1
  for i in range(len(arr)):
    if arr[i] == "K":
      last_k = i

  if arr == "K":
    return 5
  res = ""
  prev_k = True
  for i in range(len(arr)):
    if i > last_k:
      res += "1"
    else:
      if prev_k:
        res += "5"
        prev_k = False if arr[i] == "M" else True
      else:
        res += "0"
        prev_k = False if arr[i] == "M" else True

  return int(res)

arr = input()
print(minmax(arr))
print(minmin(arr))