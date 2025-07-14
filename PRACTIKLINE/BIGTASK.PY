print('Введите имя ученика:')
name = input()
print('Введите количество предметов:')
subjects = int(input())
grades = {}  # создаём пустой словарь

# Запрашиваем оценки для 3 предметов
for i in range(3):
    subject = input("Введите название предмета: ")
    grades[subject] = []  # создаём пустой список оценок для предмета

    # Запрашиваем 3 оценки для каждого предмета
    for j in range(3):
        mark = int(input(f"Введите оценку {j + 1} по предмету {subject}: "))
        grades[subject].append(mark)

# Выводим все предметы и их оценки
for subject in grades:
    print(subject, ":", grades[subject])
if subjects > 5 and subjects < 2:
    print('Оценки должны быть в диапазоне 2-5')
