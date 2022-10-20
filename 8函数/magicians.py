def show_magicians(ordinary_magicians, great_magicians):
    while ordinary_magicians:
        current_magician = ordinary_magicians.pop()

        # 输出当前魔术师的名字，并添加进great魔术师列表
        print(current_magician)
        great_magicians.append(current_magician)


def make_great(great_magicians):
    for great_magician in great_magicians:
        print("The Great " + great_magician.title() + '.')


ordinary_magicians = ['david', 'ken', 'jimi']
great_magicians = []

# 实参1为[:]列表副本,不对ordinary_magicians进行改变
show_magicians(ordinary_magicians[:], great_magicians)
make_great(great_magicians)
