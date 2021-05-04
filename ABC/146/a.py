s = input()
d = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
for i, di in enumerate(d):
    if s == di:
        print(7 - i)
        break
