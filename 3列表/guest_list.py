guset = ['jiying zheng', 'hao lin', 'xiang lin']
print('Guset List:\n\t' + guset[0].title() + '\n\t' + guset[1].title() + '\n\t' + guset[2].title())

print('\nMiss List:' + '\n\t' + guset[1].title())

guset[1] = 'ziyu zhang'
print('\nNew Guset List:\n\t' + guset[0].title() + '\n\t' + guset[1].title() + '\n\t' + guset[2].title())

print("\ncome on, " + guset[0].title() + '.')
print("come on, " + guset[1].title() + '.')
print("come on, " + guset[2].title() + '.')

print('\nI must find a bigger table.')
guset.insert(0, 'Di Wu')
guset.insert(2, 'BangBang')
guset.append('Bob')

print("\ncome on, " + guset[0].title() + '.')
print("come on, " + guset[1].title() + '.')
print("come on, " + guset[3].title() + '.')
print("come on, " + guset[4].title() + '.')
print("come on, " + guset[5].title() + '.')

print('Now I can only have dinner with two friends.')
del_friend = guset.pop()
print('sorry, '+del_friend+'.')
del_friend = guset.pop()
print('sorry, '+del_friend+'.')
del_friend = guset.pop()
print('sorry, '+del_friend+'.')
del_friend = guset.pop()
print('sorry, '+del_friend+'.')

print('come on,'+guset[0]+'.')
print('come on,'+guset[1]+'.')

del guset[0]
del guset[0]
print(guset)