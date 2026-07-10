# #? task 1
# list = [10,20,[300, 400, [5000,6000],500], 30, 40]
# list[2][2].append(7000)
# print(list)
#? task 2
# list1 = ["a", "b", ["c", ["d","e", ["f", "g"], "k"], "1"], "m", "n"]
# sub_list = ["h", "i", "j"]

# list1[2][1][2].extend(sub_list)
# print(list1)
#? task 3
# list1 = [5, 20, 15, 20, 25, 50, 20]
# for i in list1:
#     if i == 20:
#         list1.remove(20)
# print(list1)
#? task 4
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print(my_dict)
#? task 5
# dict1= {'Ten':10,'Twenty':20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# lict = [dict1]
# lict.append(dict2)
# print(lict)
#? task 6
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80,
            }
        }
    }
}
print(sampleDict['class']['students']['marks']['history'])