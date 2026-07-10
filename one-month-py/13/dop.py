def count_words(text):
    k = ""
    cnt = 0
    max1 = 0
    lict = text.split()

    for i in lict:
        cnt = len(i)
        if max1 < cnt:
            k = i
            max1 = cnt

    print(k, max1)
    return k,max1

text = str(input('Enter the text: '))

count_words(text)