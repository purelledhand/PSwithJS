word = input()
delay = 0
for i in word:
  if i == 'S':
      delay += 8
      continue
  elif (ord(i)-ord('A')) >= 19 and (ord(i)-ord('A')) <= 21:
      delay += 9
      continue
  elif (ord(i)-ord('A')) >= 22 and (ord(i)-ord('A')) <= 25:
      delay += 10
      continue
  delay += int((ord(i)-ord('A'))/3.0)+3
print(delay)