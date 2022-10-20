age = int(input('Please input your age:'))

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'Toddle'
elif age < 13:
    stage = 'child'
elif age < 20:
    stage = "teenager"
elif age < 65:
    stage = "adult"
else:
    stage = "old man"
print(stage)
