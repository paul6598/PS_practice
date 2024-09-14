def sol(a):
  k = ['a','e','u','i','o','A','O','E','I','U']
  res = 0
  for i in a:
    if i in k:
      res += 1
  return res

while True:
  a = input()
  if a == "#":
    break
  print(sol(a))