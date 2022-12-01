num = int(input('input number: '))
lst = []
for i in range((-num), num + 1):
    lst.append(i)
position1 = int(input('input position 1: '))
position2 = int(input('input position 2: '))
for i in range(len(lst)):
    if int(position1) == i + 1:
        position1 = lst[i]
    if int(position2) == i + 1:
        position2 = lst[i]
        print(position1*position2)
        break