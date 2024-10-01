n = int(input())
print(n+max(n-2,0))
for i in range(1,n+1):
  print(1,i)
if n>2:
  for i in range(2,n):
    print(n,i)