S = input().upper()
frequency = dict()
max_alpha = []

for i in S:
  if i not in frequency.keys():
    frequency[i] = S.count(i)

for i in frequency.keys():
  if frequency[i] == max(frequency.values()):
    max_alpha.append(i)

if len(max_alpha) > 1:
  print('?')
else:
  print(max_alpha[0])