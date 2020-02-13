for case in range(int(input())):
  R, str = input().split()
  alphanumeric = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:"
  P = ""

  for i in str:
    if i not in alphanumeric:
      continue
    P += i*int(R)

  print(P)