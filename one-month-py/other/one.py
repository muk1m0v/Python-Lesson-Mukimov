try:
    user_input = int(input("Enter your numbers: "))

    i = 1
    while i <=10 :
        if user_input == 0:
            print('Seccues exited!')
            break
        else:
            total = user_input + user_input
            break
    print(f'Result: {total}')
except:
    print('Error: print [int]')