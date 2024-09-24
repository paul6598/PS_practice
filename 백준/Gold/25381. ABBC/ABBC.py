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
    if a_index < index:
      res += 1
      if len(a_) == 0:
        break
      a_index = a_.popleft()

    if len(b_) == 0:
      break
    index = b_.popleft()

print(res)