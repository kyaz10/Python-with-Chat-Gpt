# Функция с параметрами по умолчанию
def power(number, degree=2):
    return number ** degree

print(power(3))      # 3 в степени 2 = 9
print(power(3, 3))   # 3 в степени 3 = 27

def person_info(name, age):
    print('Имя:', name, 'Возраст:', age)

person_info('Kyaz', 15)

#append добавляет
#remove удаляет
#
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits.remove('apple')
print(fruits)

def last_element(lst):
    return lst[-1]

# Проверяем на твоём списке фруктов:
fruits = ['banana', 'cherry', 'orange']
print(last_element(fruits))


animals = ['cat', 'dog', 'rabbit']
animals.append('tiger')
animals.remove('dog')
print(animals)

