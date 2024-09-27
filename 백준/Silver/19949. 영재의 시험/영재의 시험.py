sol = list(map(int,input().split()))

res = 0
def back(fst,snd,num,score):
  global res
  if num == 10:
    if score >= 5:
      res += 1
  else:
    for i in range(1,6):
      if fst == snd and fst == i:
        continue
      if i == sol[num]:
        back(snd,i,num+1,score+1)
      else:
        back(snd,i,num+1,score)

    
back(-1,-2,0,0)
print(res)