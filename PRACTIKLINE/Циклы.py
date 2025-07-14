for i in range(1, 11):
    print(i)

print('_____________________________________________________')

a = 1
while a <= 9:
    print(a)
    a += 1



print('_____________________________________________________')

print('Ведите число N:')
N = int(input())
total = 0
for i in range(1, N + 1):
    total += i
    print(f'Сумма чисел от 1 до {i} = {total}')


    print('_____________________________________________________')

for i in range(1, 11):
    print(f'Таблица умножения на {i}:')
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}')


n = int(input("Введите число: "))
for i in range(1, 11):
    print(f'{n} * {i} = {n * i}')

 # Игра "Угадай число"

print('Угадай число от 1 до 100:')
print('Введите число:')
while True:
    game = int(input())
    if game < 1 or game > 100:
        print('Число вне диапазона от 1 до 100. Попробуйте снова:')
    elif game < 50:
        print('Ваше число меньше нужного числа')
    elif game > 50:
        print('Ваше число больше нужного числа')
    else:
        print('Поздравляю! Вы угадали число 50!')
        break
