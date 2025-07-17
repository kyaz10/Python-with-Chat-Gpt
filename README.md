# Python Challenge with ChatGPT

📅 **Дата старта:** Июль 2025  
👤 **Автор:** Kyaza Abdurashitov  
🎯 **Цель:** Освоить Python с нуля до уверенного уровня за 30 дней вместе с ChatGPT  

---

## 📚 Пройденные темы (Дни 1–11)

| День | Темы                                                  |
|-------|------------------------------------------------------|
| 1     | print, input, строки, конкатенация                    |
| 2     | int(), арифметика, умножение                           |
| 3     | if / elif / else, логика, оценка                       |
| 4     | Циклы while, for, break, пароль                        |
| 5     | Таблица умножения, range, угадайка                     |
| 6     | def, return, параметры функций                          |
| 7     | Списки: append, remove, индексы                        |
| 8     | Циклы по спискам, upper(), матрицы                     |
| 9     | Сумма чисел, степени, таблицы, чётность                |
| 10    | Условные конструкции, фильтрация, циклы, факториал, форматированный вывод |
| 11    | lambda-функции, map(), обработка списков, задачи на функции |

---

## 🔧 Пример кода (День 11: Использование map и lambda)

```python
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
🚀 Цели курса

Пройти ключевые темы Python за 30 дней

Построить крутое портфолио на GitHub

Научиться создавать функции, списки, словари, проекты

Подготовиться к обучению в Италии на программиста

Стать разработчиком и выйти на мировой рынок

📩 Контакты
GitHub: kyaz10
Telegram: @Kyaz09

🔥 День 12 уже близко!
Дальше — словари, работа с файлами, игры и веб-разработка на Flask.
