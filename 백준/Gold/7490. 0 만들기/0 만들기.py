"""
'',+,- 를 브루트포스
"""


def dfs(n):
  res = []
  stack = [[]]
  while stack:
    tmp = stack.pop()
    if len(tmp) == n-1:
      k = ""
      for i in range(n-1):
        k += str(i+1)
        k += tmp[i]
      k += str(n)
      if eval(k) == 0:
        res.append(tmp)
    else:
      stack.append(tmp+["+"])
      stack.append(tmp+["-"])
      stack.append(tmp+[""])
  return res

t = int(input())
for _ in range(t):
  n = int(input())
  tmp = dfs(n)
  tmp.sort()
  for i in tmp:
    for num in range(n-1):
      print(num+1,end="")
      if i[num] != "":
        print(i[num],end="")
      else:
        print(" ",end="")
    print(n)
  print()
