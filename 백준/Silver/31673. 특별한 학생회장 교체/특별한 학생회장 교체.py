n,m = map(int, input().split())
vote = list(map(int, input().split()))
vote.sort(reverse = True)
tmp = 0
i = 0
while tmp < (sum(vote)+1)//2:
  tmp += vote[i]
  i += 1
i+=1
print(m//i)