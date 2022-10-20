responses = {}

# 设置一个标志，指出调查是否继续
poll_active = True

while poll_active:
    # 提示输入被调查者的姓名和信息
    name = input("\nPlease enter your name: ")
    response = input("Which mountain would you like to climb someday? ")

    # 将答案存进字典中
    responses[name] = response

    # 判断是否还有人要参与调查
    repeat = input("Would you like to let another person respond?(yes/ no) ")
    if repeat == 'no':
        poll_active = False

# 调查结束，显示结果
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name.title() + " would like to climb " + response + '.')
