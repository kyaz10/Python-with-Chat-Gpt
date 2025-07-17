# 1 задачa
a = 2
for i in range(1, 21):
    if i % 3 == 0: continue
    print(f'{i}^{a} = {i ** a}')



print()
print('Ввод:')
total = 0
for i in range(5):
    n = int(input())     # ← преобразуем в число
    if n % 2 == 0:
        total += n
print('Вывод:')
print(total)

print()

for  i in range(100, 0, -10):
        print(i)


print()
fact = 1
print('Ввод:')
n = int(input())
for i in range(1, n + 1):
    fact *= i
print('Вывод:')
print(fact)
