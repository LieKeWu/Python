# favorite_number = {
#     'Jiying': 1,
#     'Liken': 2,
#     'Di': 3,
#     'Bang': 4,
#     'Pork': 5
# }
# print("Jiying favorite number is:" + str(favorite_number['Jiying']))
# print("Liken favorite number is:" + str(favorite_number['Liken']))
# print("Di favorite number is:" + str(favorite_number['Di']))
# print("Bang favorite number is:" + str(favorite_number['Bang']))
# print("Pork favorite number is:" + str(favorite_number['Pork']))

# 修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的
# 数字打印出来。”

favorite_number = {
    'Jiying': [1, 2, 3],
    'Liken': [1, 5],
    'Di': [7, 9, 3, 2, 4],
    'Bang': [1, 0],
    'Pork': [0, 0, 7]
}

for name, numbers in favorite_number.items():
    print(name + "'s favorite number are:")
    for number in numbers:
        print('\t', number, end='')
    print()
