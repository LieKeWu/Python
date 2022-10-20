# alien_0 = {'color': 'yellow'}
# print("The alien is " + alien_0['color'] + ".")
#
# alien_0['color'] = 'blue'
# print("The alien is now " + alien_0['color'] + ".")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print('Original x_position: ' + str(alien_0['x_position']))

# 向右移动外星人
# 根据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人速度一定很快
    x_increment = 3

# 新位置=老位置+增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
