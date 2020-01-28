import sys
month, date = map(int, sys.stdin.readline().split())
date_arr = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
print(day[(sum(date_arr[:month-1])+date)%7])