numbers = [5, 12, 7, 20, 3, 9]
for i in numbers:
    if i > 10:
        print(i)
print('Готово!')

print('2 task')

def a(b):
    return b * 2
arr = [1, 2, 3]
aro = list(map(a, arr))
print(aro)

print('3 task')

def power_of_two(x):
    return x ** 2
cap = [2, 3, 4, 5]
lap = list(map(power_of_two, cap))
print(lap)

print('4 task')

def power_of_three(x):
    return x ** 3
lak = [1, 2, 3, 4]
lan = list(map(power_of_three, lak))
print(lan)

print('5 task')

def power_of_two(x):
    result = x ** 2
    print(f"{x} в квадрате = {result}")  # Показываем, что происходит
    return result

numbers = [1, 2, 3, 4, 5]
squares = list(map(power_of_two, numbers))
print("Все квадраты:", squares)

print()

def power_of_four(x):
    res = x ** 4
    print(f'{x} в 4 степени = {res}')
    return res

num = [1, 2, 3, 4]
nam = list(map(power_of_four, num))
print(nam)
