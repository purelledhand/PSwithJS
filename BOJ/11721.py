import sys

line = sys.stdin.readline()[:-1];
cnt=0;
for i in line:
    print(i, end="");
    cnt = cnt+1;
    if(cnt%10==0):
        print("");
    