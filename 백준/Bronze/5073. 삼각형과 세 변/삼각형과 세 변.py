def sol(a,b,c):
  if max(a,b,c) >= sum([a,b,c])-max(a,b,c):
    return 'Invalid'
  if a==b and b==c:
    return 'Equilateral'
  elif a==b or b==c or c==a:
    return 'Isosceles'
  return 'Scalene'

while True:
  a,b,c = map(int,input().split())
  if a+b+c == 0:
    break
  else:
    print(sol(a,b,c))  