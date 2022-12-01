st = input('input real number: ')
count = len(st)
sum = 0
if st.isdigit():
    digit = int(st)
    for i in range(count):
        sum += digit % 10
        digit //= 10
else:
    digit = float(st)
    for i in range(count):
        sum += digit // (10 ** (-i))
        digit %= (10 ** (-i))
print(sum)

