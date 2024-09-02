n = input()
z,o = 0,0
for i in n:
  if i == "0":
    z += 1
  else:
    o += 1

print("0"*(z//2)+"1"*(o//2))