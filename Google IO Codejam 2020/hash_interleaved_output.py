for case in range(1, int(input())+1):
    S = input()
    sep_io = {
        'I': 0,
        'i': 0,
        'IO': 0,
        'io': 0,
        'Io': 0,
        'iO': 0,
    }
    for i in S:
        if i == 'I' or i == 'i':
            sep_io[i] += 1
        elif i == 'O':
            if sep_io['I'] > 0:
                sep_io['I'] -= 1
                sep_io['IO'] += 1
            elif sep_io['i'] > 0:
                sep_io['i'] -= 1
                sep_io['iO'] += 1
        elif i == 'o':
            if sep_io['i'] > 0:
                sep_io['i'] -= 1
                sep_io['io'] += 1
            elif sep_io['I'] > 0:
                sep_io['I'] -= 1
                sep_io['Io'] += 1
    print("Case #{}: {}".format(case, sep_io['IO']))