from collections import deque
k = int(input())

def bfs(k):
  visit = set()
  visit.add(0)
  q = deque([[0,1,0]])
  while q:
    curr, jump, move = q.popleft()
    if curr == k:
      return move
    if (curr-jump >= -10**12) and (curr-jump not in visit):
      q.append([curr-jump,2*jump, move+1])
      visit.add(curr-jump)
    if (curr+jump <= 10**12) and (curr+jump not in visit):
      q.append([curr+jump,2*jump, move+1])
      visit.add(curr+jump)
  return -1

print(bfs(k))
