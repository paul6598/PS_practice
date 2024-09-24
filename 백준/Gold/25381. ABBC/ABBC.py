#한번 s를 탐색할때
#a와 b의 인덱스를 q에 삽입하면서 c가 나오면 b에서 하나 뽑아서 res += 1
#그 뒤 a와 b의 인덱스를 비교하면서 res에 추가

from collections import deque

a_ = deque([])
b_ = deque([])
res = 0

s = input()
for i in range(len(s)):
  if s[i] == "A":
    a_.append(i)
  elif s[i] == "B":
    b_.append(i)
  else:
    if len(b_) != 0:
      res += 1
      b_.popleft()
        
if len(b_)*len(a_) != 0:
  index = b_.popleft()
  a_index = a_.popleft()
  while True:
    #print(a_index, index)
    if a_index < index:
      res += 1
      #print(len(b_)*len(a_))
      if len(b_)*len(a_) == 0:
        break
      a_index = a_.popleft()
      index = b_.popleft()
    else:
      if len(b_)*len(a_) == 0:
        break
      index = b_.popleft()

print(res)