s = input()
key = ['Do', '', 'Re', '', 'Mi', 'Fa', '', 'So', '', 'La', '', 'Si']
p = s.find('WWBWBWW')
print(key[-(p + 1)])
