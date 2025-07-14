words = ['apple', 'banana', 'cherry']
for x in words:
    print(x.upper())

print()
for i in range(11, 21):
    if i % 2 == 0:
        print(i, '-', 'even')
    else:
        print(i, '-', 'odd')

print()

numbers = [3, 5, 7, 9]
for a in numbers:
    print(a * 4)

print()


matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
]

for le in matrix:
    for la in le:
        print(la, end=' ')
    print()
