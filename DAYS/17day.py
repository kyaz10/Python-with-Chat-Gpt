data = [55, 66, 77, 88]
data.pop(2)
print(data)
print()
user = {
    'name': 'Rustam',
    'birth': 2009,
    'city': 'Osh'
}

user.pop('birth')
print(user)

print()

grades = {
    'Timur': 89,
    'Adilet': 93,
    'Aisuluu': 88
}
lin = max(grades, key = grades.get)
top = grades[lin]
print(lin, top)

print()

week1 = {'Mon': 90, 'Tue': 110, 'Wed': 105}
week2 = {'Mon': 95, 'Tue': 120, 'Wed': 100}
total_sales = {}

for day in week1:
    total_sales[day] = week1[day] + week2.get(day, 0)

best_day = max(total_sales, key=total_sales.get)

print(best_day, total_sales[best_day])

