dic = {}
for x in range(65,91):
  dic[chr(x)] = chr(x)
for x in range(97,123):
  dic[chr(x)] = chr(x)

def sol(dic, arr):
  res = 1
  tmp = 1
  for i in range(len(arr)-1):
    if dic[arr[i]] == dic[arr[i+1]]:
      tmp += 1
      res = max(res, tmp)
    else:
      tmp = 1
  return res

arr, n = input().split()

for _ in range(int(n)):
  tmp = list(input().split())
  if tmp[0] == '2':
    print(sol(dic, arr))
  else:
    for i in dic:
      if dic[i] == tmp[1]:
        dic[i] = tmp[2]
