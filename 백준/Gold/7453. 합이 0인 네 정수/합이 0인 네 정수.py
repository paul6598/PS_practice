import sys
input = sys.stdin.readline

n = int(input())
a,b,c,d = [],[],[],[]
for _ in range(n):
  a_,b_,c_,d_ = map(int, input().split())
  a.append(a_)
  b.append(b_)
  c.append(c_)
  d.append(d_)

x,y = [],{}
for i in range(n):
  for j in range(n):
    x.append(a[i]+b[j])
    if c[i]+d[j] in y:
      y[c[i]+d[j]] += 1
    else:
      y[c[i]+d[j]] = 1


res = 0
for i in range(n*n):
 if -x[i] in y:
  res += y[-x[i]]

print(res)