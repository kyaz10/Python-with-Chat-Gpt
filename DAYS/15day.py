grades = {
    'math': [4, 5, 3, 5],
    'english': [5, 5, 4, 4],
    'physics': [3, 4, 4, 5]
}

# Удаляем по одной оценке
grades['math'].pop(3)
grades['physics'].pop(3)

# Функция для расчёта средних оценок
def average_grade(grades_dict):
    averages = {}
    for subject, marks in grades_dict.items():
        average = sum(marks) / len(marks)
        averages[subject] = round(average, 2)
    return averages

# Считаем средние
averages = average_grade(grades)
print("Средние оценки:")
for subject, avg in averages.items():
    print(f"{subject}: {avg}")

# Находим предмет с самой высокой средней
max_subject = max(averages, key=averages.get)
print(f"\nЛучший предмет по среднему баллу: {max_subject} ({averages[max_subject]})")



colors = {
    'first':'black',
    'second':'gray',
    'third':'white'
}

car = {
    'brand':'bmw',
    'model':'bmw m5 competition',
    'year':2020
}
car['colors'] = colors
print(car)