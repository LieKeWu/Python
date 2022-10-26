filename = 'search_the.txt'

# 读取文件中的the的次数，lower不区分大小写
with open(filename) as f_obj:
    the_number = f_obj.read().lower().count('the')

print(the_number)
