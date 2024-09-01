n = int(input())

if n ==1:
  print(0)
else:
  dp = [2]
  for _ in range(n-2):
    dp.append((dp[-1]*3)%1000000009)

  print(dp[-1])
  
