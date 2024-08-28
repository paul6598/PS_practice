n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

first = arr1[0]
for i in range(n):
  if arr2[i] == first:
    index = i
    break

a,b = True,True
for i in range(n):
  #print(i,(i+index)%n)
  if arr1[i] != arr2[(i+index)%n]:
    a = False
    break

for i in range(n):
  #print(i,(i+index2)%n)
  if arr1[i] != arr2[(index-i)%n]:
    b = False
    break

print("good puzzle" if a or b else "bad puzzle")