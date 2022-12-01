lst = []
for i in range(1, int(input('input number: ')) + 1):
    lst.append((round(((1 + 1 / i) ** i), 2)))
print(lst)