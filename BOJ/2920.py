P = list(map(int, input().split()))
if sorted(P) == P: print('ascending')
elif sorted(P, reverse=True) == P: print('descending')
else: print('mixed')
