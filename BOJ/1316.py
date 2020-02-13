words = []
groups = 0
index = 0
fail = False
for case in range(int(input())):
  words.append(input())

for w in words:
  index = 0
  fail = False
  while index<len(w):
    if w[w.find(w[index]):w.find(w[index])+w.count(w[index])] == w[index]*w.count(w[index]):
      index += w.count(w[index])
    else:
      fail = True
      break
  if(fail): continue
  groups += 1

print(groups)