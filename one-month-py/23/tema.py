def cnt(n):
    i = 1
    while i<=n:
        a =int(input('>>> '))
        pos,neg,zer = 0,0,0
        if a > 0:
            pos+=1
        elif 0 > a:
            neg+=1
        else:
            zer +=1

    print(f'\nNegative: {neg}')
    print(f'Positive: {pos}')
    print(f'Zero: {zer}')