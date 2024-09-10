while True:
  n = int(input())
  if n == 0:
    break
  dp = -float('INF')
  mxv = -float('INF')
  for _ in range(n):
    p = int(input())
    mxv = max(mxv,dp)
    if p > 0 and dp < 0:
      dp = p
    elif p < 0 and dp < p:
      dp = p
    else:
      dp += p
  mxv = max(mxv,dp)
  print(mxv)