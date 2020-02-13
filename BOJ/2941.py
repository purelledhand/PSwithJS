word = input()
chroa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0
index = 0
check = False

while index<len(word):
  check = False
  for i in chroa:
    if word[index:index+3].find(i) != -1:
      count += 1
      index = index+len(i)
      check = True
      break
  if check == False:
    count += 1
    index += 1

print(count)