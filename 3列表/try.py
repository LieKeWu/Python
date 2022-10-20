hardware = ['mouse', 'display', 'keyborad', 'charger']

print(len(hardware))
print(hardware[1])
hardware.append('wireless mouse')
print(hardware)
del hardware[0]
print(hardware)
miss = hardware.pop()
print(hardware)
print('miss device:'+miss)


