num = int(input('input number: '))
count = 1
sum = 1
lst = []
while count <= num:
    sum *= count
    lst.append(sum)
    count += 1
print(lst)