# while True:
#     traffic_light = input("Color: ")
#     match traffic_light:
#         case "red":
#             print("Stop!")
#         case "yellow":
#             print("Ready!")
#         case "green":
#             print("GO!")
#         case "exit":
#             break
#         case _:
#             print("Not found input")

# n = int(input("Your number: "))

# if n<0 :
#     print("error")
# else:
#     while n>=1:
#         print(n)
#         n-=1

# 

month = int(input("months : "))

match month:
    case 0:
        print("December")
    case 1:
        print("Junuary")
    case 2:
        print("Febuary")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("Jule")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("Octember")
    case 11:
        print("November")