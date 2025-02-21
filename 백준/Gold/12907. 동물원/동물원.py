n = int(input())
arr = list(map(int,input().split()))
tf = True

spc = [0 for _ in range(n)]
for i in arr:
  if n <= i:
    tf = False
    break
  else:
    spc[i] += 1

mxv = spc[0]
cnt = 0

for i in range(n):
  if spc[i] > mxv or spc[i] > 2:
    tf = False
    break
  elif spc[i] < mxv:
    mxv = spc[i]
  if spc[i] == 2:
    cnt += 1

if tf:
  if 1 in spc:
    print(2**(cnt+1))
  else:
    print(2**cnt)
else:
  print(0)
