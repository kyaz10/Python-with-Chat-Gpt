nums = [10, 20, 30, 40, 50]
nums.pop(3)
print(nums)

print()

person = {
    'name': 'Aida',
    'age': 20,
    'city': 'Bishkek'
    }
a = person.pop('age')
print(person)

print()

scores = {
    'Almaz': 65,
    'Nurlan': 72,
    'Ainura': 70
}
best = max(scores, key = scores.get)
print(f"Лучший студент: {best}")


sales_week1 = {'Mon': 100, 'Tue': 150, 'Wed': 130}
sales_week2 = {'Mon': 120, 'Tue': 140, 'Wed': 135}

total_sales = {}
for day in sales_week1:
    total_sales[day] = sales_week1[day] + sales_week2.get(day, 0)

best_day = max(total_sales, key=total_sales.get)
print(f'Лучший день: {best_day} ({total_sales[best_day]})')

print()


grades = {
    'math': 4,
    'english': 5,
    'physics': 3,
    'history': 5
}

grad = min(grades, key = grades.get)
grades.pop(grad)
print(grades)
