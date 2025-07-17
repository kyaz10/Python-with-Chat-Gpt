num = [2, 4, 6]
result = map(lambda x: x * 2, num)
print(list(result))

print('1 task')

def square(x):
    return x * x

nums = [1, 2, 3]
square = list(map(square, nums))
print(square)

print('2 task')

def a(b):
    return b * 2

arr = [1, 2, 3]
res = list(map(a, arr))
print(res)

print('3 task')

def plus(iq):
    return iq + 10

rrr = [5,10, 15]
unke = list(map(plus, rrr))
print(unke)

print('4 task')

def квадрат(y):
    return y ** 2
 
nom = [2, 3, 4]
nam = list(map(квадрат, nom))
print(nam)

print('5 task')

def minus(i):
    return -i 

min = [1, -2, 3]
mon = list(map(minus, min))
print(mon)

print('6 task')

def otris(i):
    return -abs(i)

otras = [1, -2, 3, 0, -10]
результат = list(map(otris, otras))
print(результат)

print('7 task')

def house(h):
    return len(h)

home = ['дом', 'кот', 'машина']
hom = list(map(house, home))
print(hom)

print('8 task')
num = [2, 4, 6]
result = map(lambda x: x * 2, num)
print(list(result))

print('1 task')

def square(x):
    return x * x

nums = [1, 2, 3]
square = list(map(square, nums))
print(square)

print('2 task')

def a(b):
    return b * 2

arr = [1, 2, 3]
res = list(map(a, arr))
print(res)

print('3 task')

def plus(iq):
    return iq + 10

rrr = [5,10, 15]
unke = list(map(plus, rrr))
print(unke)

print('4 task')

def квадрат(y):
    return y ** 2
 
nom = [2, 3, 4]
nam = list(map(квадрат, nom))
print(nam)

print('5 task')

def minus(i):
    return -i 

min = [1, -2, 3]
mon = list(map(minus, min))
print(mon)

print('6 task')

def otris(i):
    return -abs(i)

otras = [1, -2, 3, 0, -10]
результат = list(map(otris, otras))
print(результат)

print('7 task')

def house(h):
    return len(h)

home = ['дом', 'кот', 'машина']
hom = list(map(house, home))
print(hom)

print('8 task')
def ret(o):
    return o[::-1]

word = ['яблоко', 'машина', 'кот']
wors = list(map(ret, word))
print(wors)

print()

def pos(j):
    return

words = ['машина', 'кот']



print('9 task')

def посчитать_гласные(s):
    гласные = 'аеёиоуыэюя'
    count = 0
    for буква in s.lower():
        if буква in гласные:
            count += 1
    return count

words = ["машина", "кот", "дом", "океан"]
результат = list(map(посчитать_гласные, words))
print(результат)
