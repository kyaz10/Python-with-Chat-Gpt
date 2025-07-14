for i in range(50, 61, 2):
    print(i)

print()

a  = 3
while a < 11:
    print(a)
    a = a + 3
print()
a = int(input('Введите число:'))
for i in range(1, 11):
    print(f'{a} * {i} =', a * i)
print()
total = 0  # Создаём переменную для суммы
for i in range(1, 21):  # Цикл от 1 до 20 включительно
    total += i   # К каждому числу прибавляем сумму
print(total)  # Выводим результат
print()
print(i)
for i in range(15, 31, 2):
    print(i)
print()

number = 1
while number <= 50:
    if number % 5 == 0:
        print(number)
    number += 1

print()
a = 2
for i in range(1, 11):
     print(f'{i} - {i ** a}')