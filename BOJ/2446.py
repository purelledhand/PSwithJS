n = int(input())
for i in range(1,n+1):
    print(" "*(i-1)+"*"*((n-i+1)*2-1))
for i in range(n-1,0,-1):
    print(" "*(i-1)+"*"*((n-i+1)*2-1))