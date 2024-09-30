from collections import deque

s = int(input())
def sol(s):
  visit = [[float('inf')]*(s+1) for _ in range(s+1)]
  visit[1][0] = 0
  q = deque([[1,0,0]])
  while q:
    mnt,clip,time = q.popleft()

    if mnt+clip < s+1 and clip != 0 and visit[mnt+clip][clip] >= time+1: #클립보드 붙여넣기
      visit[mnt+clip][clip] = time+1
      q.append([mnt+clip,clip,time+1])
      if mnt+clip == s:
        return time+1


    if mnt-1>0 and visit[mnt-1][clip] >= time+1: #이모티콘 삭제
      visit[mnt-1][clip] = time+1
      q.append([mnt-1,clip,time+1])
      if mnt-1 == s:
        return time+1

    q.append([mnt,mnt,time+1]) #클립보드 저장

print(sol(s))