
game = {"Y":1,"F":2,"O":3}
n,g = input().split()

pp = set()
for _ in range(int(n)):
  pp.add(input())

print(len(pp)//game[g])