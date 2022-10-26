import json

filename = 'favorite.json'

number = float(input("请输入您喜欢的数字："))

with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)