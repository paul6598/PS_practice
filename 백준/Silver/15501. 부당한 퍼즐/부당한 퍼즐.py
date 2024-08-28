n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr3 = arr2[::-1]

first = arr1[0]
for i in range(n):
  if arr2[i] == first:
    index = i
    break

for i in range(n):
  if arr3[i] == first:
    index2 = i
    break

a,b = True,True
for i in range(n):
  #print(i,(i+index)%n)
  if arr1[i] != arr2[(i+index)%n]:
    a = False
    break
#print()
for i in range(n):
  #print(i,(i+index2)%n)
  if arr1[i] != arr3[(i+index2)%n]:
    b = False
    break

if a or b:
  print("good puzzle")
else:
  print("bad puzzle")