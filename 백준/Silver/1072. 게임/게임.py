x,y = map(int,input().split())
if y*100//x >= 99:
  print(-1)
else:
  k = y*100//x
  s,e = 0,1000000001
  while s < e:
    mid = (s+e)//2
    #print(mid)
    if k < (y+mid)*100//(x+mid) and k == (y+mid-1)*100//(x+mid-1):
      break
    elif k < (y+mid)*100//(x+mid):
      e = mid
    else:
      s = mid
  print(mid)