import random

lst = []
for i in range(int(input('input amount of elements in list: '))):
    lst.append(int(input(f'input {i} element: ')))
print('lets shuffle')
for i in range(len(lst)):
    a = lst[i]
    index = random.randint(0, len(lst) - 1)
    lst[i] = lst[index]
    lst[index] = a
print(lst)


