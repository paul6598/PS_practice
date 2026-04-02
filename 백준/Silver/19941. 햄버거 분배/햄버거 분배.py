n, k = map(int, input().split())
table = input()
burger_list = [0]*n
for i in range(len(table)):
  if table[i] == "P":
    mnv = max(0, i-k)
    mxv = min(n-1, i+k)
    for j in range(mnv, mxv+1):
      if table[j] == "H" and burger_list[j] == 0:
        burger_list[j] = 1
        break
print(sum(burger_list))