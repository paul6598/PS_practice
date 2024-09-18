def back(mxv,visit,player,num):
  if num == 11:
    return sum(visit)
  for i in range(11):
    if visit[i] == 0 and player[num][i] > 0:
      visit[i] = player[num][i]
      mxv = max(mxv,back(mxv,visit,player,num+1))
      visit[i] = 0
  return mxv


c = int(input())
for _ in range(c):
  player = []
  for _ in range(11):
    player.append(list(map(int,input().split())))
  mxv = 0
  visit = [0]*11
  print(back(mxv,visit,player,0))
  