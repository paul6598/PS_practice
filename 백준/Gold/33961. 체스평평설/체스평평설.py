m = int(input())
if m <= 2:
  print("NO")
else:
  print("YES")
  i = 0
  for _ in range(m//3-1):
    print(1,3*i+1)
    print(2,3*i+2)
    print(1,3*i+3)
    print(2,3*i+1)
    print(1,3*i+2)
    print(2,3*i+3)
    i += 1
  if m%3 == 1:
    print(1,3*i+1)
    print(2,3*i+2)
    print(1,3*i+4)
    print(2,3*i+3)
    print(1,3*i+2)
    print(2,3*i+1)
    print(1,3*i+3)
    print(2,3*i+4)
  elif m%3 == 2:
    print(1,3*i+1)
    print(2,3*i+2)
    print(1,3*i+4)
    print(2,3*i+5)
    print(1,3*i+3)
    print(2,3*i+1)
    print(1,3*i+2)
    print(2,3*i+3)
    print(1,3*i+5)
    print(2,3*i+4)
  else:
    print(1,3*i+1)
    print(2,3*i+2)
    print(1,3*i+3)
    print(2,3*i+1)
    print(1,3*i+2)
    print(2,3*i+3)

