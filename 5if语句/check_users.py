current_users = ['Ying', 'Ken', 'bob', 'Goku', 'Di']
new_users = ['Ying', 'Ken', 'Bob', 'goku', 'bang']

for new_user in new_users:
    # 列表解析 把当前用户全部小写放进列表
    if new_user.lower() in [current_user.lower() for current_user in
                            current_users]:
        print(new_user + ',The name is already in use. Please try again.')
    else:
        print(new_user + ',The name is not used, you can register.')

# # 当前用户全部小写
# for current_user in current_users:
#     print(current_user.lower())
#
# #列表解析 把当前用户全部小写放进列表
# lower_cusers = [current_user.lower() for current_user in current_users]
# print(lower_cusers)
