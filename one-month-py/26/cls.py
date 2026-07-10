# print(tuple(range(10)))
# print(tuple(range(7,10)))
# print(tuple(range(1,10,2)))

# for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
#     print(i, end=',')
# print()
# for i in range(10):
#     print(i, end=' ')

# num = int(input("Enter a number: "))

# i = 2

# while i < num:
#     if num % i == 0:
#         print('Not Prime')
#         break
#     i += 1
# else:
#     print("Prime")

# for i in range(n,0,-1):
#     print(i, end=" ") 

# num = int(input("Enter a number: "))

# cnt = 0
# for i in range(1,num + 1):
#     for x in range(1,i + 1):
#         if i % x == 0:
#             cnt+=1
#             print(i)
#     if cnt >= 3:
#         print('Not Prime')
#         break

# print("capitalize:", "hello WORLD".capitalize())
# print("casefold:", "Straße".casefold())
# print("center:", "Python".center(20, "-"))
# print("count:", "hello world, hello".count("hello"))
# print("encode:", "Привет".encode("utf-8"))
# print("endswith:", "file.txt".endswith(".txt"))
# print("expandtabs:", "col1\tcol2\tcol3".expandtabs(8))
# print("find:", "hello".find("l"))
# print("format:", "Name: {}, Age: {}".format("Alice", 30))
# data = {"name": "Bob", "age": 25}
# print("format_map:", "Name: {name}, Age: {age}".format_map(data))
# print("index:", "hello".index("e"))
# print("isalnum:", "abc123".isalnum())
# print("isalpha:", "abc".isalpha())
# print("isascii:", "abc".isascii())
# print("isdecimal:", "123".isdecimal())
# print("isdigit:", "123".isdigit())
# print("isidentifier:", "var_1".isidentifier())
# print("islower:", "hello".islower())
# print("isnumeric:", "123".isnumeric())
# print("isprintable:", "Hello\n".isprintable())
# print("isspace:", "   ".isspace())
# print("istitle:", "Hello World".istitle())
# print("isupper:", "HELLO".isupper())
# print("join:", ", ".join(["apple", "banana", "cherry"]))
# print("ljust:", "left".ljust(10, "*"))
# print("lower:", "HELLO".lower())
# print("lstrip:", "  hello  ".lstrip())
# trans_table = str.maketrans("abc", "123")
# print("maketrans:", trans_table)
# print("partition:", "one:two:three".partition(":"))
# print("replace:", "hello world".replace("world", "Python"))
# print("rfind:", "hello world hello".rfind("hello"))
# print("rindex:", "hello world hello".rindex("hello"))
# print("rjust:", "right".rjust(10, "*"))
# print("rpartition:", "one:two:three".rpartition(":"))
# print("rsplit:", "a,b,c,d".rsplit(",", 2))
# print("rstrip:", "  hello  ".rstrip())
# print("split:", "one two three".split())
# print("splitlines:", "line1\nline2\nline3".splitlines())
# print("startswith:", "file.txt".startswith("file"))
# print("strip:", "  hello  ".strip())
# print("swapcase:", "Hello World".swapcase())
# print("title:", "hello world".title())
# print("translate:", "abc".translate(trans_table))
# print("upper:", "hello".upper())
# print("zfill:", "42".zfill(5))