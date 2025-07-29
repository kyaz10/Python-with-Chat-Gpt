student = {
    'name': 'Kyaz', 
    'grade': 9
}

print(student['name'])
student['grade'] = 10
student['school'] = 'number1'
print(student)


print()

my_info = {
    "nickname": "Tiger",
    "age": 15
}

# Выводим имя
print(my_info["nickname"])  # Tiger

# Обновляем возраст
my_info["age"] = 16

# Добавляем новый ключ
my_info["goal"] = "Become Python pro"

# Удаляем ник
del my_info["nickname"]

print(my_info)
