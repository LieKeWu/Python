# print("Sarah's favorite language is " +
#       favorite_languages['sarah'].title() +
#       '.')
#
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#           language.title() + ".")
# # 默认就是keys
# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#
#     if name in friends:
#         print("\tHi " + name.title() +
#               ", I see your favorite language is " +
#               favorite_languages[name].title() + "!")
#
# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")
#
# print("The following language have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())
# “6-6 调查：在6.3.1节编写的程序favorite_languages.py中执行以下操作。
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
# 遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
#
# poll_list = ['sarah', 'ken']
# for friend in poll_list:
#     if friend in favorite_languages.keys():
#         print(friend.title() + ' thank you taking poll.')
#     else:
#         print(friend.title() + ',please take our poll.')

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c',
    'edward': ['ruby', 'go'],
    'phil': ['python', 'Java']
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(
            '\n' + name.title() + "'s favorite languages is: " + languages.title())
    else:
        print('\n' + name.title() + "'s favorite languages are:")
        for language in languages:
            print('\t' + language.title())
