def off():
    a = input('Enter the password:\n>>> ')
    cnt = 0
    char = "!@#$%^&*"
    alfav = "ABCDEFGHIJKLMNOPQRST"
    numbers = "1234567890"
    lens = False
    al = False
    num = False
    ch = False
    for i in a:
        if i in char:
            ch = True
        if i.upper() in alfav:
            al = True
        if i in numbers:
            num = True
    if len(a) >= 8:
        lens = True
    lict = [lens, al, num, ch]
    for i in lict:
        if i == True:
            cnt += 1
    if cnt == 4:
        print("Password strong")
    elif cnt >= 2 and cnt <= 3:
        print("Password is medium")
    else:
        print("Password is so Easy !!!")