word = input()
stack = []
index = 0

for i in range(int(len(word)/2)):
  stack.append(word[i])
  index += 1

if len(word)%2 != 0: index += 1

while index<len(word):
  if stack.pop() != word[index]:
    print(0)
    exit()
  index += 1

print(1)
