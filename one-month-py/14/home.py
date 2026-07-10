# #? task 1
# def IsDigit(c):
#     return '0' <= c and c <= '9'

# c = input()
# print("yes" if IsDigit(c) else "no")
#? task 2
# def user(a):
#     k = a.upper()
#     print(k)

# a = str(input(''))
# user(a)
#? task 3
# def user(a):
#     k = a.upper()
#     if a == k:
#         a = a.lower()
#         print(a)
#     else:
#         print(k)

# a = str(input(''))
# user(a)
#? task 4
# def strin(a, b):
#     if a == b:
#         print('yes')
#     else:
#         print('no')

# a = str(input(''))
# b = str(input(''))
# strin(a, b)
#? task 5
# def count_words(text):
#     return len(text)

# lict = input('').split()

# print(count_words(lict))
#? task 6
# def longest_word(text):
#     words = text.split()
#     max_word = ''
#     max_length = 0

#     for word in words:
#         if len(word) > max_length:
#             max_length = len(word)
#             max_word = word

#     print(f"{max_word}")
#     print(f"{max_length}")

# longest_word(str(input()))
#? task 7
# def pol(a):
#     if a == a[::-1]:
#         print("yes")
#     else:
#         print("no")

# a = str(input(''))
# pol(a)
#? task 8
# def lol(a):
#     for i in a:
#         if a.count(i) > 1:
#             return i

# a = input()
# print(lol(a))
#? task 9
# def off():
#     s1 = input().strip()
#     s2 = input().strip()
    
#     if s1 in s2:
#         print("yes")
#     else:
#         print("no")

# off()
#? task 10
# def off():
#     x = input().strip()
    
#     circles = {
#         '0': 1, '1': 0, '2': 0, '3': 0, '4': 1,
#         '5': 0, '6': 1, '7': 0, '8': 2, '9': 1
#     }
    
#     n = sum(circles[i] for i in x if i in circles)
#     print(n)

# off()
#? task 11
# def off():
#     s = input()
#     probel = ""

#     for cnt in s:
#         if cnt != " ":
#             probel += cnt

#     if probel == probel[::-1]:
#         print("yes")
#     else:
#         print("no")

# off()
#? task 12
# def off(lict=[]):
#     x = 0
#     y = 0
#     for i in range(0, len(lict), 2):
#         if lict[i] == 'North':
#             y += int(lict[i+1])
#         elif lict[i] == 'South':
#             y -= int(lict[i+1])
#         elif lict[i] == 'East':
#             y += int(lict[i+1])
#         elif lict[i] == 'West':
#             y -= int(lict[i+1])
#     print(x, y)

# lict = input().split()

# off(lict)
#? task 13
# def off():
#     line = input().split()
#     print(' '.join(line))

# off()
#? task 14
# def on():
#     s = input().upper()
#     k = int(input())
#     alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     r = ""
#     for c in s:
#         o = alpa.find(c) - k 
#         r += alpa[o % 26]
#     print(r)
# on()