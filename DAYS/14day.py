hui = {
    'name': 'Kyaz',
    'age' : 15,
    'hobbie' : 'book, sport, python, english',
    'city' : 'Jalal-Abad'
}

hui['goal'] = 'go abroad, and study to abroad'

del hui['hobbie']
print(hui)

print('task 2')

grades = {
    'math':4,
    'physics':5,
    'english':5
}

grades["english"] = 4   
grades["history"] = 5 

for subject, mark in grades.items():
    print(f"{subject}: {mark}")


print('3task')

store = {
    "apple": 50,
    "banana": 30,
    "milk": 90
}

store['bread'] = 60
store['milk'] = 95
total = sum(store.values())
print(f'Сумма всех товаров:{total}')

print('task4')

wrestlers = {
    "John Cena": 40,
    "The Rock": 50,
    "Roman Reigns": 38
}

wrestlers["Undertaker"] = 55
wrestlers['The Rock'] = 51
del wrestlers['John Cena']
for wrest, wrist in wrestlers.items():
    print(f'{wrest}: {wrist}')


print('last task')

def print_book(book):
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Year: {book['year']}")
    print(f"Pages: {book['pages']}")

book = {
    'title': 'Atomic Habits',
    'author': 'James Clear',
    'year': 2020,
    'pages': 250
}

print_book(book)
