n,d,k = map(int,input().split())

sell = {}
for _ in range(n):
  name, val = input().split()
  sell[name] = int(val)

ssell = dict(sorted(sell.items(), key = lambda x : -x[1]))

res = []
saving = 0
for i in ssell:
  if saving >= d:
    break
  res.append(i)
  saving += ssell[i]

if saving < d or len(res) > k:
  print('impossible')
else:
  print(len(res))
  for i in res:
    print(f"{i}, YOU ARE FIRED!")