a = float(input('Выберите первое число: '))
ab = float(input('Выберите второе число: '))

print(' 1 - Сложение')
print('2 - Вычитание')
print('3 - Умножение')
print('4 - Деление')

fun = int(input('Выберите функцию от 1 до 4:'))

if fun == 1:
    res = a + ab
elif fun == 2:
    res = a - ab
elif fun == 3:
    res = a * ab
elif fun == 4:
    res = a / ab
else:
    print('Неправильно')
print(res)