sales_week1 = {'Mon': 100, 'Tue': 150, 'Wed': 130}
sales_week2 = {'Mon': 120, 'Tue': 140, 'Wed': 135}

# Объединяем суммы по дням
total_sales = {}
for day in sales_week1:
    total_sales[day] = sales_week1[day] + sales_week2.get(day, 0)

print(total_sales)