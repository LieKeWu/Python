import json

# dump倾倒 用来存储
# load()加载

numbers = [2, 3, 5, 6, 11, 13]

filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
