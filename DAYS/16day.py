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
# Лучший студент: Nurlan (72)


sales_week1 = {'Mon': 100, 'Tue': 150, 'Wed': 130}
sales_week2 = {'Mon': 120, 'Tue': 140, 'Wed': 135}

besk = max(sales_week1, key = sales_week1.get)
belk = max(sales_week2, key = sales_week2.get)
bin = besk + belk
print(f'Лучший день: {besk}')



grades = {
    'math': 4,
    'english': 5,
    'physics': 3,
    'history': 5
}

grad = min(grades, key = grades.get)
grades.pop(grad)
print(grades)
