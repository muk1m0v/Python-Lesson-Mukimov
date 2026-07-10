# def even(x, y):
#     while x<=y:
#         if x % 2 == 1:
#             print(f'---> {x} <---')
#         x += 1

# even(int(input('First num: ')),int(input('Second num: ')))
#! Task 1
# def student(a):
#     s = str(a)
#     if s == s[::-1]:
#         return 1
#     else:
#         return 404
    
# def teacher(a):
#     a = str(a)
#     n1 = ''
#     i = -1
#     for _ in a:
#         n1+=a[i]
#         i-=1
#     if n1 == a:
#         return 1
#     else:
#         return 404
    
# def plus(a):
#     if student(a) == 1 and teacher(a) == 1 or student(a) != 1 and teacher(a) != 1:
#         print(f'---------\nYES - Is a polidrome\n---------\nStudent result: {student(a)}\nTeacher result: {teacher(a)}\n---------')
#     else:
#         print(f'---------\nNO - Is a not polidrome\n---------\nStudent result: {student(a)}\nTeacher result: {teacher(a)}\n---------')

# def check_system():
#     try:
#         a = int(input('Both input: '))
#         plus(a)
#     except:
#         print('Error: print int type')

# check_system()
#! Task 2
# def my_recursive_function(cnt=1):
#     print("test")
#     if cnt == 5:
#         return "finish"
#     cnt+=1
#     my_recursive_function (cnt)

# my_recursive_function()
#! Task 3
def my_recursive_function(i, n):
    print(i)
    if i == n:
        return "finish"
    i+=1
    my_recursive_function (i,n)

my_recursive_function(int(input('Enter the num: ')),int(input('Second num: ')))