n = int(input())
if n <= 2:
  print(4)
else:
  while n%2 == 1:
    n += 1
  print(n)